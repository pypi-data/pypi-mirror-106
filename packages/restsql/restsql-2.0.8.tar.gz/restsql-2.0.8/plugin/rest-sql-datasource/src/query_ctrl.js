import './css/query-editor.css!'

import _ from 'lodash';
import { QueryCtrl } from 'app/plugins/sdk';
import sqlPart from './sql_part';
import { PanelEvents } from '@grafana/data';

// import jQuery from 'jquery';
// const $ = jQuery;

export class RestSqlDatasourceQueryCtrl extends QueryCtrl {

  constructor($scope, $injector, uiSegmentSrv, $q) {
    super($scope, $injector);
    this.scope = $scope;
    this.uiSegmentSrv = uiSegmentSrv;
    this.$q = $q;
    this.lastQueryError = null;
    this.panelCtrl.events.on(PanelEvents.dataReceived, this.onDataReceived.bind(this), $scope);
    this.panelCtrl.events.on(PanelEvents.dataError, this.onDataError.bind(this), $scope);
    this.panelCtrl.events.on(PanelEvents.refresh, this.updateRestSqlWithoutRefresh.bind(this), $scope);
    this.target.joinQueryList = this.target.joinQueryList || [];
    this.updateProjection();

    // this.target.tableSelect = this.target.tableSelect || [];
    this.target.columnOptions = this.target.columnOptions || {};

    this.tables = [];

    this.formats = [
      { text: 'Time series', value: 'grafana.timeserie' },
      { text: 'Table', value: 'grafana.table' }
    ];
    this.types = [
      { text: 'Left Join', value: 'left_join' },
      { text: 'Inner Join', value: 'inner_join' },
      { text: 'Full Join', value: 'full_join' }
    ];

    // this.target.tableSegment = null;
    this.target.target = this.target.target || '';
    this.target.type = this.target.type || 'grafana.timeserie';

    // this.target.tableSegment = this.uiSegmentSrv.newSegment({ "value": this.target.table || 'select table', "fake": true });
    this.target.table = this.target.table || "select table";

    const from = sqlPart.create({ type: 'from', params: [this.target.table] });
    this.target.fromParts = [from];
    this.target.joinQueryList.forEach((query) => {
      const joinFrom = sqlPart.create({ type: 'from', params: [query.table.value] });
      query.fromParts = [joinFrom];
    });
    // this.selectionAdd = this.uiSegmentSrv.newPlusButton();

    this.target.selectionsParts = this.target.selectionsParts || [];
    this.selectionAdd = this.uiSegmentSrv.newPlusButton();

    this.selectMenu = [];
    this.selectMenu.push(this.uiSegmentSrv.newSegment({ type: 'expression', value: 'Expression' }));
    // this.selectionsParts = this.selectionsParts || [];
    this.target.whereParts = this.target.whereParts || [];
    this.whereAdd = this.uiSegmentSrv.newPlusButton();
    this.target.aggParts = this.target.aggParts || [];
    this.aggAdd = this.uiSegmentSrv.newPlusButton();
    this.target.groupParts = this.target.groupParts || [];
    this.groupAdd = this.uiSegmentSrv.newPlusButton();
    this.target.timeField = this.target.timeField || [];
    this.timeFieldAdd = this.uiSegmentSrv.newPlusButton();

    this.target.sortParts = this.target.sortParts || [];
    this.sortAdd = this.uiSegmentSrv.newPlusButton();
    this.target.fieldParts = this.target.fieldParts || [];
    this.fieldAdd = this.uiSegmentSrv.newPlusButton();

    // 初始化timeShift部分
    this.dimensions = [
      { text: 'second', value: 's' },
      { text: 'minute', value: 'mi' },
      { text: 'hour', value: 'h' },
      { text: 'day', value: 'd' },
      { text: 'week', value: 'w' },
      { text: 'month', value: 'mo' },
      { text: 'year', value: 'y' }
    ];

    this.target.timeAggSegment = this.uiSegmentSrv.newSegment({ "value": this.target.timeAgg || '0', "fake": true });
    this.target.timeAgg = this.target.timeAggSegment.value || '0';
    this.target.timeAggDimension = this.target.timeAggDimension || 'd';

    this.target.timeShiftSegment = this.uiSegmentSrv.newSegment({ "value": this.target.timeShift || '0', "fake": true });
    this.target.timeShift = this.target.timeShiftSegment.value || '0';
    this.target.timeShiftDimension = this.target.timeShiftDimension || 'd';

    // 初始化limit部分
    this.target.limitSegment = this.uiSegmentSrv.newSegment({ "value": this.target.limit || '1000', "fake": true });
    this.target.limit = this.target.limitSegment.value || '1000';
    this.target.queryLimitSegment = this.uiSegmentSrv.newSegment({ "value": this.target.queryLimit || '1000', "fake": true });
    this.target.queryLimit = this.target.queryLimitSegment.value || '1000';
    this.target.query = this.target.query || {
      // restSql协议结构定义
      "select": {
        "from": "",
        "filter": {},
        "group_by": [],
        "time_field": "",  // 11/6/2020: 或许将time_field字段放在这不是一个好的决定。这样对原本的restsql入侵太大了。 --oliverdding
        "aggregation": [],
        "sort": [],
      },
      "join": [],
      "sort": [],
      "fields": [],
      "limit": 200
    };
    this.variables = this.variables || {}
    this.timeFrom = this.panelCtrl.datasource.templateSrv.timeRange.from.format();
    this.timeTo = this.panelCtrl.datasource.templateSrv.timeRange.to.format();
    this.getTables(); // load available tables
    this.getColumnOptions(this.target.table);
  }


  // -----------------------------------------------------------------


  // 数据回填
  updateProjection() { // todo: 数据回填dimentions
    console.log("DEBUG: Query: updateProjection: ", this.target);
    if (this.target.target) {
      for (const key in this.target) {
        if (key.includes('Parts') && this.target[key].length > 0) {
          this.target[key].forEach((ele, index) => {
            this.target[key].splice(index, 1, sqlPart.create(ele.part))
          })
        } else if (key.includes('Segment')) {
          this.target[key] = this.uiSegmentSrv.newSegment({ "value": this.target[key].value, "fake": true })
        } else {
          this.target.type = this.target.type;
        }
      }
      if (this.target.joinQueryList.length > 0) {
        this.target.joinQueryList.forEach((ele, index) => {
          for (const key in ele) {
            if (Array.isArray(ele[key]) && ele[key].length > 0) {
              ele[key].forEach((element, i) => {
                ele[key].splice(i, 1, sqlPart.create(element.part))
              })
            } else if (key.includes('Add')) {
              ele[key] = this.uiSegmentSrv.newPlusButton()
            } else if (key === 'type') {
              ele[key] = ele.type
            } else if (key === 'table' || key === 'limit') {
              ele[key] = this.uiSegmentSrv.newSegment({ "value": ele[key].value, "fake": true })
            }
          }
        })
      }
    }
  }

  transformToSegments() {
    return (result) => {
      const segments = _.map(results, segment => {
        return this.uiSegmentSrv.newSegment({
          value: segment.text,
          expandable: segment.expandable,
        });
      });
      return segments;
    }
  }

  // Known issus 1
  onDataReceived(dataList) {
    console.log("DEBUG: Data Received:", dataList);
    this.lastQueryError = null
  }
  onDataError(err) {
    if (this.target.target) {
      this.lastQueryError = err.message
    }

  }
  // 
  getOptions() {
    const options = [];
    options.push(this.uiSegmentSrv.newSegment({ type: 'expression', value: 'Expression' }));
    return Promise.resolve(options);
  }

  removePart(parts, part) {
    const index = _.indexOf(parts, part);
    parts.splice(index, 1);
  }

  onFormatChanged() {
    // Todo: 暂时取消隐藏无关字段功能。由于无法找到页面完全载入的回调，table形式重载入时会显现。
    // if (this.target.type === 'grafana.timeserie')
    //   document.getElementById("timeSeriesSpecial").style.display = "flex";
    // else if (this.target.type === 'grafana.table')
    //   document.getElementById("timeSeriesSpecial").style.display = "none";
    this.updateRestSql();
  }
  onJoinTypeChange() {
    this.updateRestSql();
  }
  // 下拉关联
  onTableChanged(table) {
    console.log("tableChanged", table);
    this.target.table = table;
    this.getColumnOptions(table);
    this.updateRestSql();
  }

  getColumnOptions(table) { // get available fields from the given table
    this.datasource.metricFindOption(table).then(result => {
      this.target.columnOptions[table] = result.data
    })
  }

  getTables() { // get available tables from the db
    this.datasource.metricFindTables().then(result => {
      console.log("DEBUG: Available tables are: ", result.data);
      this.tables = result.data;
    })
  }

  onJoinTableChanged(joinIndex, table) {
    console.log("joinTableChanged", joinIndex);
    this.target.joinQueryList[joinIndex]["table"]["value"] = table;

    this.getColumnOptions(table);
    this.updateRestSql();
  }

  onTimeAggChanged() {
    this.target.timeAgg = this.target.timeAggSegment.value;
    this.updateRestSql();
  }

  onTimeShiftChanged() {
    this.target.timeShift = this.target.timeShiftSegment.value;
    this.updateRestSql();
  }

  onTimeAggDimensionChanged() {
    this.updateRestSql();
  }

  onTimeShiftDimensionChanged() {
    this.updateRestSql();
  }

  onLimitChanged() {
    this.target.limit = this.target.limitSegment.value;
    this.updateRestSql();
  }
  onLimitQueryChanged() {
    this.target.queryLimit = this.target.queryLimitSegment.value;
    this.updateRestSql()
  }
  onLimitJoinChanged(joinIndex) {
    this.target.joinQueryList[joinIndex].limit = this.uiSegmentSrv.newSegment({ "value": this.target.joinQueryList[joinIndex].limit.value || '1000', "fake": true });
    this.updateRestSql()
  }

  handleFromPartEvent(part, index, event) {
    if (event.name === "part-param-changed") {
      this.onTableChanged(part.params[0]);
    } else if (event.name === "get-param-options") {
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.tables));
    }
  }

  handleJoinFromPartEvent(part, joinIndex, expIndex, event) {
    if (event.name === "part-param-changed") {
      this.onJoinTableChanged(joinIndex, part.params[0]);
    } else if (event.name === "get-param-options") {
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.tables));
    }
  }

  addSelectionAction(part, index) {
    this.getOptions()
    const express = sqlPart.create({ type: 'column', params: ['column'] });
    this.target.selectionsParts.push(express);
    this.resetPlusButton(this.selectionAdd);
  }

  handleSelectionsPartEvent(part, index, event) {
    if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.removePart(this.target.selectionsParts, part);
      this.updateRestSql();
    } else if (event.name === "part-param-changed") {
      this.target.selectionsParts.forEach((item, i) => {
      })
      this.updateRestSql();
    } else if (event.name === "get-param-options") {
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[this.target.table]));
    }
  }

  addJoinSelectionAction(joinIndex, expIndex) {
    const express = sqlPart.create({ type: 'column', params: ['column'] });
    this.target.joinQueryList[joinIndex].selections.push(express)
    this.resetPlusButton(this.target.joinQueryList[joinIndex].selectionAdd);
  }

  handleJoinSelectionsPartEvent(part, joinIndex, expIndex, event) {
    if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.joinQueryList[joinIndex].selections.splice(expIndex, 1);
      this.updateRestSql()
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    } else if (event.name === "get-param-options") {
      const tableName = this.target.joinQueryList[joinIndex]["table"]["value"]
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[tableName]));
    }
  }

  addWhereAction(part, index) {
    const express = sqlPart.create({ type: 'expression', params: ['column', '=', 'value'] });
    this.target.whereParts.push(express);
    this.resetPlusButton(this.whereAdd);
  }


  handleWherePartEvent(part, index, event) {
    if (event.name === "get-param-options" && event.param.name === "op") {
      const operators = ['=', '<', '<=', '>', '>=', 'CONTAINS', 'STARTSWITH', 'ENDSWITH', 'RANGE', 'IN'];
      return Promise.resolve(this.uiSegmentSrv.newOperators(operators));
    } else if (event.name === "get-param-options" && event.param.name === "left") {
      // 左值为可选列
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[this.target.table]));
    } else if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.whereParts.splice(index, 1);
      this.updateRestSql()
    } else if (event.name === "part-param-changed") {
      console.log(part, index, '😎');
      this.updateRestSql();
    } else {
      return Promise.resolve([]);
    }
  }

  addJoinWhereAction(joinIndex, expIndex) {
    const express = sqlPart.create({ type: 'expression', params: ['column', '=', 'value'] });
    this.target.joinQueryList[joinIndex].where.push(express);
    this.resetPlusButton(this.target.joinQueryList[joinIndex].whereAdd);
  }

  handleJoinWherePartEvent(part, joinIndex, expIndex, event) {
    console.log("handleJoinWherePartEvent", event);
    if (event.name === "get-param-options" && event.param.name === "op") {
      const operators = ['=', '<', '<=', '>', '>=', 'CONTAINS', 'STARTSWITH', 'ENDSWITH', 'RANGE', 'IN'];
      return Promise.resolve(this.uiSegmentSrv.newOperators(operators));
    } else if (event.name === "get-param-options" && event.param.name === "left") {
      // 左值为可选列
      const tableName = this.target.joinQueryList[joinIndex]["table"]["value"]
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[tableName]));
    } else if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.joinQueryList[joinIndex].where.splice(expIndex, 1);
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    } else {
      return Promise.resolve([]);
    }
  }

  addAggAction() {
    const express = sqlPart.create({ type: 'aggregate', params: ['avg', 'column'] });
    console.log("addAggAction", express);
    this.target.aggParts.push(express);
    this.resetPlusButton(this.aggAdd);
  }

  handleAggPartEvent(part, index, event) {
    console.log("handleAggPartEvent", event, part, index);
    if (event.name === "get-param-options" && event.param.name === "agg") {
      // 暂时只支持展开操作符列表
      const operators = event.param.options;
      return Promise.resolve(this.uiSegmentSrv.newOperators(operators));
    } else if (event.name === "get-param-options" && event.param.name === "column") {
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[this.target.table]));
    } else if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.aggParts.splice(index, 1)
      this.updateRestSql()
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    } else {
      return Promise.resolve([]);
    }
  }

  addJoinAggAction(joinIndex) {
    const express = sqlPart.create({ type: 'aggregate', params: ['avg', 'column'] });
    console.log("addJoinAggAction", express);
    this.target.joinQueryList[joinIndex].aggs.push(express);
    this.resetPlusButton(this.target.joinQueryList[joinIndex].aggAdd);
  }

  handleJoinAggPartEvent(part, joinIndex, expIndex, event) {
    console.log("handleJoinAggPartEvent", event);
    if (event.name === "get-param-options" && event.param.name === "agg") {
      // 暂时只支持展开操作符列表
      const operators = event.param.options;
      return Promise.resolve(this.uiSegmentSrv.newOperators(operators));
    } else if (event.name === "get-param-options" && event.param.name === "column") {
      // 左值为可选列
      const tableName = this.target.joinQueryList[joinIndex]["table"]["value"]
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[tableName]));
    } else if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.joinQueryList[joinIndex].aggs.splice(expIndex, 1);
      this.updateRestSql()
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    } else {
      return Promise.resolve([]);
    }
  }

  addGroupAction() {
    const express = sqlPart.create({ type: 'column', params: ['column'] });
    console.log("addGroupsAction", express);
    this.target.groupParts.push(express);
    this.resetPlusButton(this.groupAdd);
  }

  addTimeFieldAction() {
    const express = sqlPart.create({ type: 'column', params: ['column'] });
    console.log("addTimeFieldAction", express);
    this.target.timeField.push(express);
    this.resetPlusButton(this.timeFieldAdd);
  }

  handleGroupPartEvent(part, index, event) {
    // console.log("handleGroupsPartEvent");
    if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "get-param-options") {
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[this.target.table]));
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.groupParts.splice(index, 1);
      this.updateRestSql()
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    }
  }

  handleTimeFieldEvent(part, index, event) {
    // console.log("handleTimeFieldEvent");
    if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "get-param-options") {
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[this.target.table]));
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.timeField.splice(index, 1);
      this.updateRestSql()
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    }
  }

  addJoinGroupAction(part, joinIndex, expIndex) {
    const express = sqlPart.create({ type: 'column', params: ['column'] });
    console.log("addGroupsAction", express);
    this.target.joinQueryList[joinIndex].groups.push(express);
    this.resetPlusButton(this.target.joinQueryList[joinIndex].groupAdd);
  }

  handleJoinGroupPartEvent(part, joinIndex, expIndex, event) {
    if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "get-param-options") {
      // 左值为可选列
      const tableName = this.target.joinQueryList[joinIndex]["table"]["value"]
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.target.columnOptions[tableName]));
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.joinQueryList[joinIndex].groups.splice(expIndex, 1);
      this.updateRestSql();
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    }
  }

  addJoinOnAction(part, joinIndex, expIndex) {
    const express = sqlPart.create({ type: 'on', params: ['field', 'field'] });
    this.target.joinQueryList[joinIndex].on.push(express);
    this.resetPlusButton(this.target.joinQueryList[joinIndex].onAdd);
  }

  handleJoinOnPartEvent(part, joinIndex, expIndex, event) {
    console.log("handleJoinOnPartEvent", event);
    if (event.name === "get-param-options" && event.param.name === "op") {
      // 暂时只支持展开操作符列表
      const operators = ['='];
      return Promise.resolve(this.uiSegmentSrv.newOperators(operators));
    } else if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.joinQueryList[joinIndex].on.splice(expIndex, 1);
    } else if (event.name === "get-param-options" && event.param.name === "field2") {
      // on field1=field2，field2是join的表中的字段，field1是原始表中的字段，这里做成可选项
      console.log("handleJoinOnPartEvent", this.target.joinQueryList[joinIndex]);
      const options = [];
      this.target.joinQueryList[joinIndex].selections.forEach((part) => {
        options.push(part["params"][0]);
      });
      return Promise.resolve(this.uiSegmentSrv.newOperators(options));
    } else if (event.name === "get-param-options" && event.param.name === "field1") {
      const options = [];
      this.target.selectionsParts.forEach((part) => {
        options.push(part["params"][0]);
      });
      return Promise.resolve(this.uiSegmentSrv.newOperators(options));
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    } else {
      return Promise.resolve([]);
    }
  }

  addJoinExportAction(part, joinIndex, expIndex) {
    const express = sqlPart.create({ type: 'alias', params: ['fields', 'alias'] });
    this.target.joinQueryList[joinIndex].export.push(express);
    this.resetPlusButton(this.target.joinQueryList[joinIndex].exportAdd);
  }
  onJoinLimitChanged(joinIndex) {
    this.target.joinQueryList[joinIndex].limit = this.target.joinQueryList[joinIndex].limit.value;
    this.updateRestSql();
  }

  handleJoinExportPartEvent(part, joinIndex, expIndex, event) {
    console.log("handleJoinExportPartEvent", event);
    if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.joinQueryList[joinIndex].export.splice(expIndex, 1);
      this.updateRestSql();
    } else if (event.name === "get-param-options" && event.param.name === "field") {
      const options = this.getExportOptions(this.target.joinQueryList[joinIndex].selections, this.target.joinQueryList[joinIndex].aggs);
      return Promise.resolve(this.uiSegmentSrv.newOperators(options));
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    } else {
      return Promise.resolve([]);
    }
  }

  addSortAction(index) {
    const express = sqlPart.create({ type: 'sort', params: ['asc', 'field'] });
    console.log("addSortAction", index);
    this.target.sortParts.push(express);
    this.resetPlusButton(this.sortAdd);
  }

  handleSortPartEvent(part, index, event) {
    console.log("handleSortPartEvent", event);
    if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {
      this.target.sortParts.splice(index, 1);
      this.updateRestSql();
    } else if (event.name === "get-param-options" && event.param.name === "field") {
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.getAllFields()));
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    } else {
      return Promise.resolve([]);
    }
  }

  addFieldAction(index) {
    const express = sqlPart.create({ type: 'alias', params: ['fields', 'alias'] });
    this.target.fieldParts.push(express);
    this.resetPlusButton(this.fieldAdd);
  }

  handleFieldPartEvent(part, index, event) {
    if (event.name === "get-part-actions") {
      return this.$q.when([{ text: 'Remove', value: 'remove' }]);
    } else if (event.name === "action" && event.action.value === "remove") {

      this.target.fieldParts.splice(index, 1);
      this.updateRestSql();

    } else if (event.name === "get-param-options" && event.param.name === "field") {
      console.log("DEBUG: Query: Field: ", this.uiSegmentSrv.newOperators(this.getAllFields()));
      return Promise.resolve(this.uiSegmentSrv.newOperators(this.getAllFields()));
    } else if (event.name === "get-param-options" && event.param.name === "alias") {
      return Promise.resolve(this.uiSegmentSrv.newOperators(['exclude']));
    } else if (event.name === "part-param-changed") {
      this.updateRestSql();
    } else {
      return Promise.resolve([]);
    }
  }

  resetPlusButton(button) {
    const plusButton = this.uiSegmentSrv.newPlusButton();
    button.html = plusButton.html;
    button.value = plusButton.value;
  }

  addJoin() {
    const queryObj = {
      type: "left_join",
      fromParts: [sqlPart.create({ type: 'from', params: ['select table'] })],
      table: this.uiSegmentSrv.newPlusButton(),
      selections: [],
      selectionAdd: this.uiSegmentSrv.newPlusButton(),
      where: [],
      whereAdd: this.uiSegmentSrv.newPlusButton(),
      aggs: [],
      aggAdd: this.uiSegmentSrv.newPlusButton(),
      groups: [],
      groupAdd: this.uiSegmentSrv.newPlusButton(),
      on: [],
      onAdd: this.uiSegmentSrv.newPlusButton(),
      export: [],
      exportAdd: this.uiSegmentSrv.newPlusButton(),
      limit: this.uiSegmentSrv.newSegment({ "value": '1000', "fake": true }),
    };
    this.target.joinQueryList.push(queryObj);
  }
  delJoin(index) {
    this.target.joinQueryList.splice(index, 1)
  }

  getAllFields() {
    // 获取select的字段，aggregate的字段，以及所有join表中的export字段
    const mainFields = this.getExportOptions(this.target.selectionsParts, this.target.aggParts);
    const exportFields = []
    this.target.joinQueryList.forEach((query) => {
      console.log("fafadsf1", query.export)
      query.export.forEach((part) => {
        console.log("fafadsf2", part);
        exportFields.push(part.params[1]) // todo: 重复元素保护
      });
    });
    return mainFields.concat(exportFields)
  }

  getExportOptions(selections, aggs) {
    // 获取select的字段和aggs的字段并格式化为restSql格式
    const options = [];
    selections.forEach((part) => {
      // export已经select的字段
      options.push(part["params"][0]);
    });
    aggs.forEach((part) => {
      // export已经aggregation的字段
      console.log("handleJoinExportPartEvent", part);
      const [aggFunc, field] = part.params;
      options.push([field, aggFunc].join("__"));
    });
    return options;
  }

  updateRestSql() {
    this.updateRestSqlWithoutRefresh();
    if (this.target.query.fields !== null &&
      this.target.query.fields !== undefined &&
      this.target.query.fields !== "") { // only refresh when fields in filled.
      this.panelCtrl.refresh();
    }
  }

  isJson(inputStr) {
    try {
      if (typeof JSON.parse(inputStr) == "object") {
        return true;
      }
    } catch (e) {
    }
    return false;
  }

  handleWhereParts(parts) {
    let whereTarget = {};
    const operatorToSuffix = {
      "=": "",
      "<": "__lt",
      "<=": "__lte",
      ">": "__gt",
      ">=": "__gte",
      "CONTAINS": "__contains",
      "STARTSWITH": "__startswith",
      "ENDSWITH": "__endswith",
      "RANGE": "__range",
      "IN": "__in"
    }
    parts.forEach((part) => {
      const suffix = operatorToSuffix[part.params[1]];
      const key = `${part.params[0]}${suffix}`;
      let value = part.params[2];
      if (this.isJson(value)) {
        // 操作符为IN和RANGE时，右值为json数组的形式
        const valueList = JSON.parse(value);
        if (!Array.isArray(valueList)) {
          return Promise.reject(new Error("Error: Only support array type"));
        }
        whereTarget[key] = valueList;
      } else {
        if ((value.startsWith("\"") && value.endsWith("\"")) || (value.startsWith("\'") && value.endsWith("\'"))) {
          // 字符串处理，删除头尾手动添加的单/双引号
          const tmpStr = value;
          whereTarget[key] = tmpStr.slice(1, tmpStr.length - 1);
        } else if (!isNaN(Number(value))) {
          whereTarget[key] = Number(value);
        } else if (value.toLowerCase() === "true") {
          whereTarget[key] = true;
        } else if (value.toLowerCase() === "false") {
          whereTarget[key] = false;
        } else if (value.startsWith("$")) {
          whereTarget[key] = value;
        } else if (value.match(/^\[.*\$.*\]$/g)) {
          whereTarget[key] = value
        }
        else {
          return Promise.reject(new Error("Error: input string is invalid"));
        }
      }
    });
    return whereTarget;
  }

  updateRestSqlWithoutRefresh() {
    // 将输入的内容更新到target中去
    this.target.query = {
      // restSql协议结构定义
      "select": {
        "from": "",
        "fields": [],
        "filter": {},
        "group_by": [],
        "time_field": "",
        "aggregation": [],
        "sort": [],
      },
      "join": [],
      "sort": [],
      "fields": [],
      "limit": 200
    };

    // udpate table
    this.target.query.select.from = this.target.table;

    // update queryLimit
    this.target.query.select.limit = parseInt(this.target.queryLimit);

    // update select fields
    this.target.selectionsParts.forEach((part) => {
      this.target.query.select.fields.push(part.params[0]);
    });

    // update time range
    this.timeFrom = this.panelCtrl.datasource.templateSrv.timeRange.from.format();
    this.timeTo = this.panelCtrl.datasource.templateSrv.timeRange.to.format();
    console.log("updaterestsql", this.timeFrom, this.timeTo);

    this.target.query.select.filter = this.handleWhereParts(this.target.whereParts);

    // update aggregation
    // todo:agg func无法修改, 无法删除
    this.target.aggParts.forEach((part) => {
      const [aggFunc, field] = part.params;
      this.target.query.select.aggregation.push([field, aggFunc].join("__"));
    });

    // update group by
    this.target.groupParts.forEach((part) => {
      console.log("groupParts", part);
      this.target.query.select.group_by.push(part.params[0]);
    });

    // update timefield
    this.target.timeField.forEach((part) => {// todo: 当前方案是多timefield但是只取第一个作为实际timefield值
      this.target.query.select.time_field = part.params[0];
    });

    // update join
    this.target.joinQueryList.forEach((query) => {
      const joinQuery = {};
      // update join type
      joinQuery.type = query.type;
      joinQuery.query = { "select": {} };
      // update join table
      joinQuery.query.select.from = query.table.value;
      // update join fields
      joinQuery.query.select.fields = []
      query.selections.forEach((part) => {
        joinQuery.query.select.fields.push(part.params[0]);
      });
      // udpate join filter
      joinQuery.query.select.filter = {};
      joinQuery.query.select.filter = this.handleWhereParts(query.where);
      // update aggregation 
      // todo:agg func无法修改
      joinQuery.query.select.aggregation = [];
      query.aggs.forEach((part) => {
        const [aggFunc, field] = part.params;
        joinQuery.query.select.aggregation.push([field, aggFunc].join("__"));
      });
      // update join group by
      joinQuery.query.select.group_by = [];
      query.groups.forEach((part) => {
        joinQuery.query.select.group_by.push(part.params[0]);
      });
      // update join on
      joinQuery.on = {};
      query.on.forEach((part) => {
        joinQuery.on[part.params[0]] = part.params[1];
      });
      // updaate export
      joinQuery.export = [];
      query.export.forEach((part) => {
        joinQuery.export.push(part.params.join("@"));
      });
      // update joinLimit
      joinQuery.limit = parseInt(query.limit.value);
      this.target.query.join.push(joinQuery);
    });

    // update sort
    this.target.sortParts.forEach((part) => {
      const sortExp = part.params[0] === "asc" ? part.params[1] : `-${part.params[1]}`;
      this.target.query.sort.push(sortExp);
    });

    //update fields
    this.target.fieldParts.forEach((part) => {
      this.target.query.fields.push(part.params.join("@"));
    });

    // update limit
    this.target.query.limit = parseInt(this.target.limit);
    this.target.target = JSON.stringify(this.target.query);
    // this.target.target = this.target.query;
  }

}
RestSqlDatasourceQueryCtrl.templateUrl = 'partials/query.editor.html';

