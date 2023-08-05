import _ from 'lodash';

class SqlPartDef {
  constructor(options) {
    this.type = options.type;
    if (options.label) {
      this.label = options.label;
    } else {
      this.label = this.type[0].toUpperCase() + this.type.substring(1) + ':';
    }
    this.style = options.style;
    if (this.style === 'function') {
      this.wrapOpen = '(';
      this.wrapClose = ')';
      this.separator = ', ';
    } else if (this.style === 'alias') {
        this.separator = ' as ';
    } else if (this.style === 'on') {
        this.separator = ' = ';
    } else if (this.style === 'aggregate') {
      this.separator = ' (';
      this.wrapClose = ')';
    } else {
      this.wrapOpen = ' ';
      this.wrapClose = ' ';
      this.separator = ' ';
    } 
    this.params = options.params;
    this.defaultParams = options.defaultParams;
  }
}

class SqlPart {
  constructor(part, def) {
    this.part = part;
    this.def = def;
    if (!this.def) {
      throw { message: 'Could not find sql part ' + part.type };
    }

    this.datatype = part.datatype;

    if (part.name) {
      this.name = part.name;
      this.label = def.label + ' ' + part.name;
    } else {
      this.name = '';
      this.label = def.label;
    }

    part.params = part.params || _.clone(this.def.defaultParams);
    this.params = part.params;
  }

  updateParam(strValue, index) {
    // handle optional parameters
    if (strValue === '' && this.def.params[index].optional) {
      this.params.splice(index, 1);
    } else {
      this.params[index] = strValue;
    }

    this.part.params = this.params;
  }
}


const index = [];

function createPart(part) {
  // console.log("createPartHAHA", part);
  const def = index[part.type];
  if (!def) {
    return null;
  }

  return new SqlPart(part, def);
}

function register(options) {
  index[options.type] = new SqlPartDef(options);
}

register({
  type: 'column',
  style: 'label',
//   params: [{ type: 'column', dynamicLookup: true }],
  params: [{ type: 'string', dynamicLookup: true }],
  defaultParams: ['value'],
});

register({
  type: 'from',
  style: 'label',
  label: 'Table:',
  params: [
    { name: 'table', type: 'string', dynamicLookup: true },
  ],
  defaultParams: ['test'],
});

register({
  type: 'expression',
  style: 'expression',
  label: 'Expr:',
  params: [
    { name: 'left', type: 'string', dynamicLookup: true },
    { name: 'op', type: 'string', dynamicLookup: true },
    { name: 'right', type: 'string', dynamicLookup: true },
  ],
  defaultParams: ['value1', '>', 'value2'],
});

register({
  type: 'macro',
  style: 'label',
  label: 'Macro:',
  params: [],
  defaultParams: [],
});

register({
  type: 'aggregate',
  style: 'label',
  label: 'Agg:',
  params: [
    {
      name: 'agg',
      type: 'string',
      options: ['avg', 'sum', 'max', 'min','count', 'count_distinct'],
      dynamicLookup: true
    },
    { name: 'column', type: 'string', dynamicLookup: true }
  ],
  defaultParams: ['avg', 'column'],
});

register({
  type: 'alias',
  style: 'alias',
  params: [
      { name: 'field', type: 'string',  dynamicLookup: true },
      { name: 'alias', type: 'string',  dynamicLookup: true }
  ],
  defaultParams: ['alias'],
});

register({
    type: 'on',
    style: 'on',
    params: [
        { name: 'field1', type: 'string',  dynamicLookup: true },
        { name: 'field2', type: 'string',  dynamicLookup: true }
    ],
  });

register({
type: 'sort',
style: 'sort',
label: 'Order by:',
params: [
    { name: 'sort', type: 'string',  options: ['asc', 'desc'], dynamicLookup: true },
    { name: 'field', type: 'string',  dynamicLookup: true }
],
});
  



export default {
  create: createPart,
};
