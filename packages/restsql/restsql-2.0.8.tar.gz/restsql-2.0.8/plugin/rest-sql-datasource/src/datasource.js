import _ from "lodash";
import { resultsToDataFrames } from "@grafana/data";

export class RestSqlDatasource {

  /*
    query(option): panel查询数据
    testDatasource(): 数据源页面验证数据源可用
    annotationQuery(options): dashboard获取注释信息
    metricFindQuery(options): 查询编辑页面获取提示信息
  */

  constructor(instanceSettings, $q, backendSrv, templateSrv) {
    console.log("------ DataSource ------");
    console.log("instanceSettings: ", instanceSettings);
    console.log("backendSrv: ", backendSrv);
    console.log("templateSrv: ", templateSrv);
    console.log("------ DataSource ------");
    this.type = instanceSettings.type;
    this.url = instanceSettings.url;
    this.name = instanceSettings.name;
    this.q = $q;
    this.backendSrv = backendSrv;
    this.templateSrv = templateSrv;
    this.withCredentials = instanceSettings.withCredentials;
    this.headers = { 'Content-Type': 'application/json' };
    if (typeof instanceSettings.basicAuth === 'string' && instanceSettings.basicAuth.length > 0) {
      this.headers['Authorization'] = instanceSettings.basicAuth;
    }
  }

  isJson(inputStr) {
    try {
      if (typeof JSON.parse(inputStr) === "object") {
        return true;
      }
    } catch (e) {
    }
    return false;
  }

  getAllVariables(varName) {
    console.log("getAllVariables: varName:", varName);
    const varList = [];
    this.templateSrv.variables.forEach((variable) => {
      if (variable.name === varName.substring(1)) {
        variable.options.forEach((option) => {
          if (option.value !== "$__all") {
            varList.push(option.value);
          }
        });

      }
    });
    return JSON.stringify(varList);
  }

  getQueryStr(target, timeshift) {
    /*
      提取所有的where语句，暂时只在where中支持变量与时间范围
      2020.10.18: options.targets是数组，多query时使用
      2020.10.19: 修改传入参数为target, 将调用细分
      2020.10.23 timeShift初次解决：增加timeShift=true/false控制缩放
      2020.10.24 timeShift二次解决：使用timeShift, timeShiftDimension控制shift
      2020.10.27 timeAgg
      2020.11.6 修复时间戳转换过程中少8小时的bug
      2020.11.7 将自动填充时间戳改为yyyy-mm-ddTHH:MM:SS.SSSZ格式
      */
    console.log("DEBUG: Query Variable: target:  ", target);
    const queryJson = JSON.parse(target.target);
    const filters = queryJson['select']['filter'];
    // timeFrom、timeTo就是query panel右上方的时间控制变量
    const timeFromOrig = new Date(this.templateSrv.timeRange.from + timeshift); // timestamp
    const timeFrom = `${timeFromOrig.getFullYear().toString().padStart(4,'0')}-${(timeFromOrig.getMonth() + 1).toString().padStart(2,'0')}-${timeFromOrig.getDate().toString().padStart(2,'0')}T${timeFromOrig.getHours().toString().padStart(2,'0')}:${timeFromOrig.getMinutes().toString().padStart(2,'0')}:${timeFromOrig.getSeconds().toString().padStart(2,'0')}.000Z`;
    const timeToOrig = new Date(this.templateSrv.timeRange.to + timeshift);
    const timeTo = `${timeToOrig.getFullYear().toString().padStart(4,'0')}-${(timeToOrig.getMonth() + 1).toString().padStart(2,'0')}-${timeToOrig.getDate().toString().padStart(2,'0')}T${timeToOrig.getHours().toString().padStart(2,'0')}:${timeToOrig.getMinutes().toString().padStart(2,'0')}:${timeToOrig.getSeconds().toString().padStart(2,'0')}.000Z`;
    // variables就是左上方的用户自定义变量
    const variables = {};
    this.templateSrv.variables.forEach(ele => {
      const key = "$" + ele.name;
      variables[key] = ele.current.value;
    });
    console.log("DEBUG: Query Variable: time: ", timeFrom, timeTo);
    // 主查询语句variables替换
    Object.keys(filters).map((key) => {
      if (typeof filters[key] !== "number") { // todo: warning: 每次只能匹配到一个值，但是后面又用循环处理
        const varList = filters[key].match(/\$(__)*[a-zA-Z]+/g);
        console.log("DEBUG: datasource: queryStr: ", varList);
        if (varList) {
          varList.forEach((varItem) => {
            if (Object.keys(variables).includes(varItem)) {
              let varValue = variables[varItem];
              if (Array.isArray(varValue) && varValue.length > 1) {
                // 变量多选时，变量值为Array
                filters[key] = JSON.stringify(varValue);
              } else {
                filters[key] = filters[key].replace(varItem, varValue);
                if (filters[key] === "$__all") {
                  // 变量选择”All“
                  console.log("change all value");
                  filters[key] = this.getAllVariables(varItem);
                }
              }
            } else if (["$__timeFrom"].includes(varItem)) {
              filters[key] = filters[key].replace(varItem, `${timeFrom}`);
            } else if (["$__timeTo"].includes(varItem)) {
              filters[key] = filters[key].replace(varItem, `${timeTo}`);
            }
          });
        }
        if (this.isJson(filters[key])) {
          filters[key] = JSON.parse(filters[key]);
        } else if (filters[key].startsWith("\"") && filters[key].endsWith("\"")) {
          // 删除前后多余的引号
          filters[key] = filters[key].substring(1, filters[key].length - 1);
        }
      }
    });
    const joinQueries = queryJson['join']
    joinQueries.forEach((query) => {
      const joinFilters = query['query']['select']['filter']
      Object.keys(joinFilters).map((key) => {
        if (typeof joinFilters[key] !== "number") {
          const varList = joinFilters[key].match(/\$(__)*[a-zA-Z]+/g);
          if (varList) {
            varList.forEach((varItem) => {
              if (Object.keys(variables).includes(varItem)) {
                let varValue = variables[varItem];
                if (Array.isArray(varValue) && varValue.length > 1) {
                  // 变量多选时，变量值为Array
                  joinFilters[key] = JSON.stringify(varValue);
                } else {
                  joinFilters[key] = joinFilters[key].replace(varItem, varValue);
                  if (joinFilters[key] === "$__all") {
                    // 变量选择”All“
                    console.log("change all value");
                    joinFilters[key] = this.getAllVariables(varItem);
                  }
                }

              } else if (["$__timeFrom"].includes(varItem)) {
                joinFilters[key] = joinFilters[key].replace(varItem, `'${timeFrom}'`);
              } else if (["$__timeTo"].includes(varItem)) {
                joinFilters[key] = joinFilters[key].replace(varItem, `'${timeTo}'`);
              }
            });
          }
          console.log("filteris", joinFilters);
          if (this.isJson(joinFilters[key])) {
            joinFilters[key] = JSON.parse(joinFilters[key]);
          }
        }
      });
    })
    // return JSON.stringify(queryJson);
    return queryJson;
  }

  query(options) {
    console.log("DEBUG: Query: Original Options: ", options);
    // var query = this.buildQueryParameters(options);
    if (options.targets.length <= 0) {
      return this.q.when({ data: [] });
    }

    const payload = { // todo: 删除多余target.type
      format: options.targets[0].type
    };
    const data = new Array(); // 多query支持
    options.targets.forEach(target => {
      if (target.type === 'grafana.timeserie') { // type == 'grafana.timeserie'
        payload.beginTime = options.range.from.valueOf().toString();
        payload.endTime = options.range.from.valueOf().toString();
        var timeshift = parseInt(target.timeShift); // have to put here: getQueryStr need timeshift
        if (target.query.select.time_field !== null &&
          target.query.select.time_field !== undefined &&
          target.query.select.time_field !== "") { // timefield exists
          var inWherePart = false;
          var timefield = target.query.select.time_field;
          console.log("DEBUG: TimeField exists. ", timefield);
          for (var key in target.query.select.filter) {
            if (key.search(timefield) !== -1) { // mark if timefield in where parts
              inWherePart = true;
              break;
            }
          }
          // timeshift字段用于两处：1. 前端shift下，让query能query到shift后的数据。2. 后端shift下，让后端能把数据x轴shift回当前的窗口
          if (!inWherePart) { // not in where parts
            console.log("DEBUG: timefield not in where parts");
            if (timeshift !== 0) { // timeshift exists
              console.log("DEBUG: find timeshift");
              const timeShiftDimension = target.timeShiftDimension;
              switch (timeShiftDimension) {
                case "s":
                  timeshift = timeshift * 1000;
                  break;
                case "mi":
                  timeshift = timeshift * 60 * 1000;
                  break;
                case "h":
                  timeshift = timeshift * 60 * 60 * 1000;
                  break;
                case "d":
                  timeshift = timeshift * 24 * 60 * 60 * 1000;
                  break;
                case "w":
                  timeshift = timeshift * 7 * 24 * 60 * 60 * 1000;
                  break;
                case "mo":
                  timeshift = timeshift * 30 * 7 * 24 * 60 * 60 * 1000;
                  break;
                case "y":
                  timeshift = timeshift * 365 * 24 * 60 * 60 * 1000;
                  break;
              }
            }
            // fill in where parts
            target.query.select.filter[timefield + "__gte"] = "$__timeFrom";
            target.query.select.filter[timefield + "__lte"] = "$__timeTo";
          }
          // fill in select, group by and fields part
          target.query.select.fields.push(timefield);
          target.query.select.group_by.push(timefield);
          target.query.fields.push(timefield + "@" + timefield);
          console.log("DEBUG: Finish: autofill: ", target);
        }
        delete target.query.select.time_field;
        target.target = JSON.stringify(target.query); // update query to target
        const aPayLoad = {
          query: this.getQueryStr(target, timeshift),
          timeShift: parseInt(target.timeShift),
          timeShiftDimension: target.timeShiftDimension,
          timeAgg: parseInt(target.timeAgg),
          timeAggDimension: target.timeAggDimension
        }; // Time不应该放这的
        data.push(aPayLoad);
      } else if (target.type === 'grafana.table') {
        const aPayLoad = {
          query: this.getQueryStr(target, 0)
        };
        data.push(aPayLoad);
      }
    });
    payload.data = data;

    console.log("DEBUG: Query: Payload: ", payload);
    return this.doRequest({
      url: this.url + '/query',
      method: 'POST',
      data: payload
    }).then((resp) => {
      if (resp.data.status === "error") {
        return Promise.reject(new Error(resp.data.msg));
      } else if (resp.data.status === "ok") {
        console.log("DEBUG: Query: Received: ", resp.data);
        return resp.data;
      }
    });
  }

  testDatasource() {
    return this.doRequest({
      url: this.url + '/',
      method: 'GET',
    }).then(response => {
      if (response.status === 200) {
        return { status: "success", message: "Restsql server is ready!", title: "Success" };
      }
    });
  }

  /*
    annotationQuery(options) {
      var query = this.templateSrv.replace(options.annotation.query, {}, 'glob');
      var annotationQuery = {
        range: options.range,
        annotation: {
          name: options.annotation.name,
          datasource: options.annotation.datasource,
          enable: options.annotation.enable,
          iconColor: options.annotation.iconColor,
          query: query
        },
        rangeRaw: options.rangeRaw
      };
   
      return this.doRequest({
        url: this.url + '/annotations',
        method: 'POST',
        data: annotationQuery
      }).then(result => {
        return result.data;
      });
    }
  */

  metricFindQuery(query) {
    /*
        
    */
    //console.log("metricFindQuery", query);
    const payload = {
      "target": this.templateSrv.replace(query, null, 'regex')
    };

    console.log("metricFindQuery", payload);
    return this.doRequest({
      url: this.url + '/search',
      data: payload,
      method: 'POST',
    }).then((resp) => {
      if (resp && resp.data && resp.data.status === "error") {
        return Promise.reject(new Error(resp.data.msg));
      } else if (resp && resp.data && resp.data.status === "ok") {
        return this.mapToTextValue(resp.data);
      } else {
        return [];
      }
    });
  }


  // 下拉选项
  metricFindOption(tableName) {
    const payload = {
      tableName
    }
    return this.doRequest({
      url: this.url + '/find_options',
      method: 'POST',
      data: payload
    }).then((resp) => {
      if (resp.data.status === "error") {
        return Promise.reject(new Error(resp.data.msg));
      } else if (resp.data.status === "ok") {
        return resp.data;
      }
    });
    ;
  }

  metricFindTables() {
    return this.doRequest({
      url: this.url + '/find_tables',
      method: 'GET',
    }).then((resp) => {
      if (resp.data.status === "error") {
        return Promise.reject(new Error(resp.data.msg));
      } else if (resp.data.status === "ok") {
        return resp.data;
      }
    });
  }



  mapToTextValue(result) {
    /*
        用于metricFindQuery调整下拉选框
    */
    console.log('metricFindQuery received: ', result);
    return _.map(result.data, (d, i) => {
      if (d && d.text && d.value) {
        return { text: d.text, value: d.value };
      } else if (_.isObject(d)) {
        return { text: d, value: i };
      }
      return { text: d, value: d };
    });
  }

  doRequest(options) {
    options.withCredentials = this.withCredentials;
    options.headers = this.headers;
    return this.backendSrv.datasourceRequest(options);
  }

  // filter targets.target
  buildQueryParameters(options) {
    options.targets = _.filter(options.targets, target => {
      return target.target !== 'select metric';
    });

    var targets = _.map(options.targets, target => {
      const queryRow = this.templateSrv.replace(target.target, options.scopedVars, 'regex');
      var query = JSON.parse(queryRow);
      if (query.select.aggregation.length > 0) {
        this.filterAggregation(query.select.aggregation)
      }
      query.join.forEach(element => {
        if (element.query.select.aggregation.length > 0) {
          this.filterAggregation(element.query.select.aggregation)
        }
      });
      return {
        target: JSON.stringify(query),
        // target: query,
        refId: target.refId,
        hide: target.hide,
        type: target.type || 'timeserie'
      };
    });

    options.targets = targets;

    return options;
  }


  //  filter query aggregation
  filterAggregation(array) {
    const varables = []
    this.templateSrv.variables.forEach(ele => {
      varables.push({
        name: '$' + ele.name,
        value: ele.current.value
      })
    });
    varables.forEach(element => {
      if (array.length > 0) {
        array.forEach((ele, index) => {
          console.log(ele, element, '222');
          if (ele.startsWith(element.name)) {
            var field = ele.split('__')
            field[0] = "(" + element.value.join(',') + ")"
            array.splice(index, 1, [field[0], field[1]].join('__'))
          }
        })
      }

    })
  }

  /*
    getTagKeys(options) {
      return new Promise((resolve, reject) => {
        this.doRequest({
          url: this.url + '/tag-keys',
          method: 'POST',
          data: options
        }).then(result => {
          return resolve(result.data);
        });
      });
    }
  
    getTagValues(options) {
      return new Promise((resolve, reject) => {
        this.doRequest({
          url: this.url + '/tag-values',
          method: 'POST',
          data: options
        }).then(result => {
          return resolve(result.data);
        });
      });
    }
  */
}
