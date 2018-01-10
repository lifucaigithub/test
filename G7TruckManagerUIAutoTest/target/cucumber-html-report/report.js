$(document).ready(function() {var formatter = new CucumberHTML.DOMFormatter($('.cucumber-report'));formatter.uri("Module01_G7TruckManagerPasswordModify/Case01_G7TruckManagerLogin.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "手机管车登录",
  "description": "",
  "id": "手机管车登录",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "完成登录",
  "description": "",
  "id": "手机管车登录;完成登录",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "页面出现输入框,我输入\"\u003caccount\u003e\"和\"\u003cpassword\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 8,
  "name": "",
  "description": "",
  "id": "手机管车登录;完成登录;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "account",
        "password",
        "button",
        "title"
      ],
      "line": 9,
      "id": "手机管车登录;完成登录;;1"
    },
    {
      "cells": [
        "登录",
        "登录",
        "lifucai",
        "Qq123123",
        "登录",
        "手机管车"
      ],
      "line": 10,
      "id": "手机管车登录;完成登录;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 10,
  "name": "完成登录",
  "description": "",
  "id": "手机管车登录;完成登录;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"登录\"页,直到\"登录\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "页面出现输入框,我输入\"lifucai\"和\"Qq123123\"",
  "matchedColumns": [
    2,
    3
  ],
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我点击\"登录\"",
  "matchedColumns": [
    4
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"手机管车\"出现",
  "matchedColumns": [
    5
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 3
    },
    {
      "val": "登录",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 3859007857,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "lifucai",
      "offset": 12
    },
    {
      "val": "Qq123123",
      "offset": 22
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.find_textFields(String,String)"
});
formatter.result({
  "duration": 31913969580,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 554495170,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 2990899212,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case02_G7TruckManagerLoginMy.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "到达我的手机管车和钱包页面",
  "description": "",
  "id": "到达我的手机管车和钱包页面",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "到达我的页面",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 5,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 6,
  "name": "",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面;",
  "rows": [
    {
      "cells": [
        "button",
        "title"
      ],
      "line": 7,
      "id": "到达我的手机管车和钱包页面;到达我的页面;;1"
    },
    {
      "cells": [
        "我的",
        "我的手机管车"
      ],
      "line": 8,
      "id": "到达我的手机管车和钱包页面;到达我的页面;;2"
    },
    {
      "cells": [
        "我的钱包",
        "平安易宝"
      ],
      "line": 9,
      "id": "到达我的手机管车和钱包页面;到达我的页面;;3"
    },
    {
      "cells": [
        "平安易宝",
        "平安交易服务"
      ],
      "line": 10,
      "id": "到达我的手机管车和钱包页面;到达我的页面;;4"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 8,
  "name": "到达我的页面",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我点击\"我的\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 5,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 738701105,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 628695103,
  "status": "passed"
});
formatter.scenario({
  "line": 9,
  "name": "到达我的页面",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面;;3",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我点击\"我的钱包\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 5,
  "name": "我应该看到\"平安易宝\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的钱包",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 442236061,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "平安易宝",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 518765856,
  "status": "passed"
});
formatter.scenario({
  "line": 10,
  "name": "到达我的页面",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面;;4",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我点击\"平安易宝\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 5,
  "name": "我应该看到\"平安交易服务\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "平安易宝",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 542694581,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "平安交易服务",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 3089550873,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 11,
  "name": "到达我的页面",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 12,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 13,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 14,
  "name": "",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面;",
  "rows": [
    {
      "cells": [
        "title"
      ],
      "line": 15,
      "id": "到达我的手机管车和钱包页面;到达我的页面;;1"
    },
    {
      "cells": [
        "平安易宝"
      ],
      "line": 16,
      "id": "到达我的手机管车和钱包页面;到达我的页面;;2"
    },
    {
      "cells": [
        "我的手机管车"
      ],
      "line": 17,
      "id": "到达我的手机管车和钱包页面;到达我的页面;;3"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 16,
  "name": "到达我的页面",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 12,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 13,
  "name": "我应该看到\"平安易宝\"出现",
  "matchedColumns": [
    0
  ],
  "keyword": "那么"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_leftMenu()"
});
formatter.result({
  "duration": 3248696843,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "平安易宝",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 61740681,
  "status": "passed"
});
formatter.scenario({
  "line": 17,
  "name": "到达我的页面",
  "description": "",
  "id": "到达我的手机管车和钱包页面;到达我的页面;;3",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 12,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 13,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    0
  ],
  "keyword": "那么"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_leftMenu()"
});
formatter.result({
  "duration": 393253172,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 993773052,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case03_G7TruckManagerLoginMyDriver.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "我的司机",
  "description": "",
  "id": "我的司机",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "我的司机页面",
  "description": "",
  "id": "我的司机;我的司机页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 7,
  "name": "",
  "description": "",
  "id": "我的司机;我的司机页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 8,
      "id": "我的司机;我的司机页面;;1"
    },
    {
      "cells": [
        "我的",
        "我的手机管车",
        "我的司机",
        "我的司机"
      ],
      "line": 9,
      "id": "我的司机;我的司机页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 9,
  "name": "我的司机页面",
  "description": "",
  "id": "我的司机;我的司机页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"我的\"页,直到\"我的手机管车\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击\"我的司机\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"我的司机\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的",
      "offset": 3
    },
    {
      "val": "我的手机管车",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 425371892,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的司机",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 497721679,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的司机",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1889381745,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case04_G7TruckManagerLoginMyDriverAdd.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "添加司机",
  "description": "",
  "id": "添加司机",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 4,
  "name": "进入添加司机信息页面",
  "description": "",
  "id": "添加司机;进入添加司机信息页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 8,
  "name": "",
  "description": "",
  "id": "添加司机;进入添加司机信息页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 9,
      "id": "添加司机;进入添加司机信息页面;;1"
    },
    {
      "cells": [
        "我的司机",
        "我的司机",
        "添加",
        "司机信息"
      ],
      "line": 10,
      "id": "添加司机;进入添加司机信息页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 10,
  "name": "进入添加司机信息页面",
  "description": "",
  "id": "添加司机;进入添加司机信息页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"我的司机\"页,直到\"我的司机\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我点击\"添加\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"司机信息\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的司机",
      "offset": 3
    },
    {
      "val": "我的司机",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 211328459,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "添加",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 223164302,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "司机信息",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 775120766,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 12,
  "name": "添加司机",
  "description": "",
  "id": "添加司机;添加司机",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 13,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 14,
  "name": "司机页面输入\"\u003cdriverName\u003e\"和\"\u003cphone\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 15,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 16,
  "name": "我等待\u003ctime\u003e秒",
  "keyword": "当"
});
formatter.step({
  "line": 17,
  "name": "我应该看到\"\u003cdriverName\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 18,
  "name": "",
  "description": "",
  "id": "添加司机;添加司机;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "driverName",
        "phone",
        "button",
        "time",
        "driverName"
      ],
      "line": 19,
      "id": "添加司机;添加司机;;1"
    },
    {
      "cells": [
        "司机信息",
        "司机信息",
        "Alih",
        "13730645598",
        "保存",
        "8000",
        "Alih"
      ],
      "line": 20,
      "id": "添加司机;添加司机;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 20,
  "name": "添加司机",
  "description": "",
  "id": "添加司机;添加司机;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 13,
  "name": "我在\"司机信息\"页,直到\"司机信息\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 14,
  "name": "司机页面输入\"Alih\"和\"13730645598\"",
  "matchedColumns": [
    2,
    3
  ],
  "keyword": "当"
});
formatter.step({
  "line": 15,
  "name": "我点击\"保存\"",
  "matchedColumns": [
    4
  ],
  "keyword": "当"
});
formatter.step({
  "line": 16,
  "name": "我等待8000秒",
  "matchedColumns": [
    5
  ],
  "keyword": "当"
});
formatter.step({
  "line": 17,
  "name": "我应该看到\"Alih\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "司机信息",
      "offset": 3
    },
    {
      "val": "司机信息",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 302699133,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "Alih",
      "offset": 7
    },
    {
      "val": "13730645598",
      "offset": 14
    }
  ],
  "location": "G7TruckManagerAddDriverRelevantStepDefs.add_driver(String,String)"
});
formatter.result({
  "duration": 12343055596,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "保存",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 925476092,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "8000",
      "offset": 3
    }
  ],
  "location": "G7TruckManagerOtherRelevantStepDefs.waitTime(int)"
});
formatter.result({
  "duration": 8002081748,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "Alih",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 70849501,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case05_G7TruckManagerLoginMyDriverDelete.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "删除某个司机",
  "description": "",
  "id": "删除某个司机",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 4,
  "name": "删除某个司机",
  "description": "",
  "id": "删除某个司机;删除某个司机",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我删除司机\"\u003cdriverName\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我等待\u003ctime\u003e秒",
  "keyword": "当"
});
formatter.step({
  "line": 8,
  "name": "我不应该看到\"\u003cdriverName\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 9,
  "name": "",
  "description": "",
  "id": "删除某个司机;删除某个司机;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "driverName",
        "time",
        "driverName"
      ],
      "line": 10,
      "id": "删除某个司机;删除某个司机;;1"
    },
    {
      "cells": [
        "我的司机",
        "我的司机",
        "Alih",
        "8000",
        "Alih"
      ],
      "line": 11,
      "id": "删除某个司机;删除某个司机;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 11,
  "name": "删除某个司机",
  "description": "",
  "id": "删除某个司机;删除某个司机;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"我的司机\"页,直到\"我的司机\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我删除司机\"Alih\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我等待8000秒",
  "matchedColumns": [
    3
  ],
  "keyword": "当"
});
formatter.step({
  "line": 8,
  "name": "我不应该看到\"Alih\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的司机",
      "offset": 3
    },
    {
      "val": "我的司机",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 158087915,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "Alih",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerAddDriverRelevantStepDefs.delete_driver(String)"
});
formatter.result({
  "duration": 2890106453,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "8000",
      "offset": 3
    }
  ],
  "location": "G7TruckManagerOtherRelevantStepDefs.waitTime(int)"
});
formatter.result({
  "duration": 8000696593,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "Alih",
      "offset": 7
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.delete_driver_success(String)"
});
formatter.result({
  "duration": 401417285,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case06_G7TruckManagerLoginMyDriverDeleteBackToMy.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "我的司机回退到我的",
  "description": "",
  "id": "我的司机回退到我的",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "我的司机页面",
  "description": "",
  "id": "我的司机回退到我的;我的司机页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 7,
  "name": "",
  "description": "",
  "id": "我的司机回退到我的;我的司机页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "title"
      ],
      "line": 8,
      "id": "我的司机回退到我的;我的司机页面;;1"
    },
    {
      "cells": [
        "我的司机",
        "我的司机",
        "我的手机管车"
      ],
      "line": 9,
      "id": "我的司机回退到我的;我的司机页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 9,
  "name": "我的司机页面",
  "description": "",
  "id": "我的司机回退到我的;我的司机页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"我的司机\"页,直到\"我的司机\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的司机",
      "offset": 3
    },
    {
      "val": "我的司机",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 272118631,
  "status": "passed"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_leftMenu()"
});
formatter.result({
  "duration": 417616990,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1053855027,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case07_G7TruckManagerLoginMyInfo.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "到达我的信息页面",
  "description": "",
  "id": "到达我的信息页面",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "到达我的信息页面",
  "description": "",
  "id": "到达我的信息页面;到达我的信息页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 7,
  "name": "",
  "description": "",
  "id": "到达我的信息页面;到达我的信息页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 8,
      "id": "到达我的信息页面;到达我的信息页面;;1"
    },
    {
      "cells": [
        "我的",
        "我的手机管车",
        "我的信息",
        "我的信息"
      ],
      "line": 9,
      "id": "到达我的信息页面;到达我的信息页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 9,
  "name": "到达我的信息页面",
  "description": "",
  "id": "到达我的信息页面;到达我的信息页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"我的\"页,直到\"我的手机管车\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击\"我的信息\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"我的信息\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的",
      "offset": 3
    },
    {
      "val": "我的手机管车",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 492949054,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 467628035,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 707743077,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case08_G7TruckManagerMyInfoDetail.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "我的信息页面元素检查",
  "description": "",
  "id": "我的信息页面元素检查",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "到达我的信息页面",
  "description": "",
  "id": "我的信息页面元素检查;到达我的信息页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我应该看到\"\u003ckeywords1\u003e\"出现",
  "keyword": "那么"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"\u003ckeywords2\u003e\"出现",
  "keyword": "那么"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"\u003ckeywords3\u003e\"出现",
  "keyword": "那么"
});
formatter.step({
  "line": 8,
  "name": "我应该看到\"\u003ckeywords4\u003e\"出现",
  "keyword": "那么"
});
formatter.step({
  "line": 9,
  "name": "我应该看到\"\u003ckeywords5\u003e\"出现",
  "keyword": "那么"
});
formatter.step({
  "line": 10,
  "name": "我应该看到\"\u003ckeywords6\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 11,
  "name": "",
  "description": "",
  "id": "我的信息页面元素检查;到达我的信息页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "keywords1",
        "keywords2",
        "keywords3",
        "keywords4",
        "keywords5",
        "keywords6"
      ],
      "line": 12,
      "id": "我的信息页面元素检查;到达我的信息页面;;1"
    },
    {
      "cells": [
        "我的信息",
        "我的信息",
        "机构",
        "姓名",
        "手机号",
        "邮箱",
        "修改密码",
        "退出登录"
      ],
      "line": 13,
      "id": "我的信息页面元素检查;到达我的信息页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 13,
  "name": "到达我的信息页面",
  "description": "",
  "id": "我的信息页面元素检查;到达我的信息页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"我的信息\"页,直到\"我的信息\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我应该看到\"机构\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"姓名\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"手机号\"出现",
  "matchedColumns": [
    4
  ],
  "keyword": "那么"
});
formatter.step({
  "line": 8,
  "name": "我应该看到\"邮箱\"出现",
  "matchedColumns": [
    5
  ],
  "keyword": "那么"
});
formatter.step({
  "line": 9,
  "name": "我应该看到\"修改密码\"出现",
  "matchedColumns": [
    6
  ],
  "keyword": "那么"
});
formatter.step({
  "line": 10,
  "name": "我应该看到\"退出登录\"出现",
  "matchedColumns": [
    7
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 3
    },
    {
      "val": "我的信息",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 491567023,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "机构",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 169649316,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "姓名",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 77089390,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "手机号",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 45019312,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "邮箱",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 75752876,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "修改密码",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 112100245,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "退出登录",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 45169697,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case09_G7TruckManagerPasswordModifyPage.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "修改密码",
  "description": "",
  "id": "修改密码",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "点击修改密码",
  "description": "",
  "id": "修改密码;点击修改密码",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 7,
  "name": "",
  "description": "",
  "id": "修改密码;点击修改密码;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 8,
      "id": "修改密码;点击修改密码;;1"
    },
    {
      "cells": [
        "我的信息",
        "我的信息",
        "修改密码",
        "原始密码"
      ],
      "line": 9,
      "id": "修改密码;点击修改密码;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 9,
  "name": "点击修改密码",
  "description": "",
  "id": "修改密码;点击修改密码;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"我的信息\"页,直到\"我的信息\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击\"修改密码\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"原始密码\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 3
    },
    {
      "val": "我的信息",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 180336069,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "修改密码",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 404946662,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "原始密码",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 803402197,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 14,
  "name": "修改密码",
  "description": "",
  "id": "修改密码;修改密码",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 15,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 16,
  "name": "我在第\u003cn\u003e个输入框输入\"\u003ckeywords1\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 17,
  "name": "我在第\u003cn1\u003e个输入框输入\"\u003ckeywords2\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 18,
  "name": "我在第\u003cn2\u003e个输入框输入\"\u003ckeywords3\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 19,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 20,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 23,
  "name": "",
  "description": "",
  "id": "修改密码;修改密码;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "n",
        "n1",
        "n2",
        "keywords1",
        "keywords2",
        "keywords3",
        "button",
        "title"
      ],
      "line": 24,
      "id": "修改密码;修改密码;;1"
    },
    {
      "cells": [
        "修改密码",
        "修改密码",
        "1",
        "2",
        "3",
        "Qq123123",
        "Qq123456",
        "Qq123456",
        "确定",
        "原始密码"
      ],
      "line": 25,
      "id": "修改密码;修改密码;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 25,
  "name": "修改密码",
  "description": "",
  "id": "修改密码;修改密码;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 15,
  "name": "我在\"修改密码\"页,直到\"修改密码\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 16,
  "name": "我在第1个输入框输入\"Qq123123\"",
  "matchedColumns": [
    2,
    5
  ],
  "keyword": "当"
});
formatter.step({
  "line": 17,
  "name": "我在第2个输入框输入\"Qq123456\"",
  "matchedColumns": [
    3,
    6
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 18,
  "name": "我在第3个输入框输入\"Qq123456\"",
  "matchedColumns": [
    4,
    7
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 19,
  "name": "我点击\"确定\"",
  "matchedColumns": [
    8
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 20,
  "name": "我应该看到\"原始密码\"出现",
  "matchedColumns": [
    9
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "修改密码",
      "offset": 3
    },
    {
      "val": "修改密码",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 118175469,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "1",
      "offset": 3
    },
    {
      "val": "Qq123123",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.enter_oneTextFields(int,String)"
});
formatter.result({
  "duration": 5317116968,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "2",
      "offset": 3
    },
    {
      "val": "Qq123456",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.enter_oneTextFields(int,String)"
});
formatter.result({
  "duration": 5902799093,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "3",
      "offset": 3
    },
    {
      "val": "Qq123456",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.enter_oneTextFields(int,String)"
});
formatter.result({
  "duration": 5574462103,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "确定",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 854932271,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "原始密码",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 998879917,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 29,
  "name": "修改密码页返回",
  "description": "",
  "id": "修改密码;修改密码页返回",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 30,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 31,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 32,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 35,
  "name": "",
  "description": "",
  "id": "修改密码;修改密码页返回;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "title"
      ],
      "line": 36,
      "id": "修改密码;修改密码页返回;;1"
    },
    {
      "cells": [
        "修改密码",
        "修改密码",
        "我的信息"
      ],
      "line": 37,
      "id": "修改密码;修改密码页返回;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 37,
  "name": "修改密码页返回",
  "description": "",
  "id": "修改密码;修改密码页返回;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 30,
  "name": "我在\"修改密码\"页,直到\"修改密码\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 31,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 32,
  "name": "我应该看到\"我的信息\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "修改密码",
      "offset": 3
    },
    {
      "val": "修改密码",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 198937037,
  "status": "passed"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_leftMenu()"
});
formatter.result({
  "duration": 305872850,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 650506380,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 39,
  "name": "退出登录",
  "description": "",
  "id": "修改密码;退出登录",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 40,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 41,
  "name": "我点击\"\u003cbutton1\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 42,
  "name": "我点击\"\u003cbutton2\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 43,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 46,
  "name": "",
  "description": "",
  "id": "修改密码;退出登录;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button1",
        "button2",
        "title"
      ],
      "line": 47,
      "id": "修改密码;退出登录;;1"
    },
    {
      "cells": [
        "我的信息",
        "退出登录",
        "退出登录",
        "确认退出",
        "登录"
      ],
      "line": 48,
      "id": "修改密码;退出登录;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 48,
  "name": "退出登录",
  "description": "",
  "id": "修改密码;退出登录;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 40,
  "name": "我在\"我的信息\"页,直到\"退出登录\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 41,
  "name": "我点击\"退出登录\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 42,
  "name": "我点击\"确认退出\"",
  "matchedColumns": [
    3
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 43,
  "name": "我应该看到\"登录\"出现",
  "matchedColumns": [
    4
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 3
    },
    {
      "val": "退出登录",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 499142980,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "退出登录",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 451789344,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "确认退出",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 1531561579,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 356053915,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 50,
  "name": "手机管车登录",
  "description": "",
  "id": "修改密码;手机管车登录",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 51,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 52,
  "name": "页面出现输入框,我输入\"\u003caccount\u003e\"和\"\u003cpassword\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 53,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 54,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 55,
  "name": "",
  "description": "",
  "id": "修改密码;手机管车登录;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "account",
        "password",
        "button",
        "title"
      ],
      "line": 56,
      "id": "修改密码;手机管车登录;;1"
    },
    {
      "cells": [
        "登录",
        "登录",
        "lifucai",
        "Qq123456",
        "登录",
        "手机管车"
      ],
      "line": 57,
      "id": "修改密码;手机管车登录;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 57,
  "name": "手机管车登录",
  "description": "",
  "id": "修改密码;手机管车登录;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 51,
  "name": "我在\"登录\"页,直到\"登录\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 52,
  "name": "页面出现输入框,我输入\"lifucai\"和\"Qq123456\"",
  "matchedColumns": [
    2,
    3
  ],
  "keyword": "当"
});
formatter.step({
  "line": 53,
  "name": "我点击\"登录\"",
  "matchedColumns": [
    4
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 54,
  "name": "我应该看到\"手机管车\"出现",
  "matchedColumns": [
    5
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 3
    },
    {
      "val": "登录",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 850404189,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "lifucai",
      "offset": 12
    },
    {
      "val": "Qq123456",
      "offset": 22
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.find_textFields(String,String)"
});
formatter.result({
  "duration": 31262280641,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 370107613,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 2067300934,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 61,
  "name": "到达我的手机管车页面",
  "description": "",
  "id": "修改密码;到达我的手机管车页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 62,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 63,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 64,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 65,
  "name": "",
  "description": "",
  "id": "修改密码;到达我的手机管车页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 66,
      "id": "修改密码;到达我的手机管车页面;;1"
    },
    {
      "cells": [
        "管车首页",
        "手机管车",
        "我的",
        "我的手机管车"
      ],
      "line": 67,
      "id": "修改密码;到达我的手机管车页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 67,
  "name": "到达我的手机管车页面",
  "description": "",
  "id": "修改密码;到达我的手机管车页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 62,
  "name": "我在\"管车首页\"页,直到\"手机管车\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 63,
  "name": "我点击\"我的\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 64,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "管车首页",
      "offset": 3
    },
    {
      "val": "手机管车",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 724115481,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 288476308,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 922704443,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 69,
  "name": "到达我的信息页面",
  "description": "",
  "id": "修改密码;到达我的信息页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 70,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 71,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 72,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 73,
  "name": "",
  "description": "",
  "id": "修改密码;到达我的信息页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 74,
      "id": "修改密码;到达我的信息页面;;1"
    },
    {
      "cells": [
        "我的手机管车",
        "我的手机管车",
        "我的信息",
        "我的信息"
      ],
      "line": 75,
      "id": "修改密码;到达我的信息页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 75,
  "name": "到达我的信息页面",
  "description": "",
  "id": "修改密码;到达我的信息页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 70,
  "name": "我在\"我的手机管车\"页,直到\"我的手机管车\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 71,
  "name": "我点击\"我的信息\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 72,
  "name": "我应该看到\"我的信息\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 3
    },
    {
      "val": "我的手机管车",
      "offset": 15
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 130332611,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 423328075,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 537676072,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 77,
  "name": "点击修改密码",
  "description": "",
  "id": "修改密码;点击修改密码",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 78,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 79,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 80,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 81,
  "name": "",
  "description": "",
  "id": "修改密码;点击修改密码;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 82,
      "id": "修改密码;点击修改密码;;1"
    },
    {
      "cells": [
        "我的信息",
        "修改密码",
        "修改密码",
        "原始密码"
      ],
      "line": 83,
      "id": "修改密码;点击修改密码;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 83,
  "name": "点击修改密码",
  "description": "",
  "id": "修改密码;点击修改密码;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 78,
  "name": "我在\"我的信息\"页,直到\"修改密码\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 79,
  "name": "我点击\"修改密码\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 80,
  "name": "我应该看到\"原始密码\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 3
    },
    {
      "val": "修改密码",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 185667844,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "修改密码",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 409424764,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "原始密码",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 548497147,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 85,
  "name": "修改密码",
  "description": "",
  "id": "修改密码;修改密码",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 86,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 87,
  "name": "我在第\u003cn\u003e个输入框输入\"\u003ckeywords1\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 88,
  "name": "我在第\u003cn1\u003e个输入框输入\"\u003ckeywords2\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 89,
  "name": "我在第\u003cn2\u003e个输入框输入\"\u003ckeywords3\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 90,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 91,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 94,
  "name": "",
  "description": "",
  "id": "修改密码;修改密码;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "n",
        "n1",
        "n2",
        "keywords1",
        "keywords2",
        "keywords3",
        "button",
        "title"
      ],
      "line": 95,
      "id": "修改密码;修改密码;;1"
    },
    {
      "cells": [
        "修改密码",
        "修改密码",
        "1",
        "2",
        "3",
        "Qq123456",
        "Qq123123",
        "Qq123123",
        "确定",
        "原始密码"
      ],
      "line": 96,
      "id": "修改密码;修改密码;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 96,
  "name": "修改密码",
  "description": "",
  "id": "修改密码;修改密码;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 86,
  "name": "我在\"修改密码\"页,直到\"修改密码\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 87,
  "name": "我在第1个输入框输入\"Qq123456\"",
  "matchedColumns": [
    2,
    5
  ],
  "keyword": "当"
});
formatter.step({
  "line": 88,
  "name": "我在第2个输入框输入\"Qq123123\"",
  "matchedColumns": [
    3,
    6
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 89,
  "name": "我在第3个输入框输入\"Qq123123\"",
  "matchedColumns": [
    4,
    7
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 90,
  "name": "我点击\"确定\"",
  "matchedColumns": [
    8
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 91,
  "name": "我应该看到\"原始密码\"出现",
  "matchedColumns": [
    9
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "修改密码",
      "offset": 3
    },
    {
      "val": "修改密码",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 145112354,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "1",
      "offset": 3
    },
    {
      "val": "Qq123456",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.enter_oneTextFields(int,String)"
});
formatter.result({
  "duration": 5278999779,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "2",
      "offset": 3
    },
    {
      "val": "Qq123123",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.enter_oneTextFields(int,String)"
});
formatter.result({
  "duration": 5598925434,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "3",
      "offset": 3
    },
    {
      "val": "Qq123123",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.enter_oneTextFields(int,String)"
});
formatter.result({
  "duration": 5474526140,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "确定",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 864084376,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "原始密码",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1053376203,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 98,
  "name": "返回至我的信息页面",
  "description": "",
  "id": "修改密码;返回至我的信息页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 99,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 100,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 101,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 104,
  "name": "",
  "description": "",
  "id": "修改密码;返回至我的信息页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "title"
      ],
      "line": 105,
      "id": "修改密码;返回至我的信息页面;;1"
    },
    {
      "cells": [
        "修改密码",
        "修改密码",
        "我的信息"
      ],
      "line": 106,
      "id": "修改密码;返回至我的信息页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 106,
  "name": "返回至我的信息页面",
  "description": "",
  "id": "修改密码;返回至我的信息页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 99,
  "name": "我在\"修改密码\"页,直到\"修改密码\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 100,
  "name": "我点击回退",
  "keyword": "当"
});
formatter.step({
  "line": 101,
  "name": "我应该看到\"我的信息\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "修改密码",
      "offset": 3
    },
    {
      "val": "修改密码",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 271191327,
  "status": "passed"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_leftMenu()"
});
formatter.result({
  "duration": 301761119,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 557122234,
  "status": "passed"
});
formatter.uri("Module01_G7TruckManagerPasswordModify/Case10_G7TruckManagerMyInfo.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language: zh-CN"
    }
  ],
  "line": 2,
  "name": "退出登录",
  "description": "",
  "id": "退出登录",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "退出登录",
  "description": "",
  "id": "退出登录;退出登录",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击\"\u003cbutton1\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我点击\"\u003cbutton2\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 10,
  "name": "",
  "description": "",
  "id": "退出登录;退出登录;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button1",
        "button2",
        "title"
      ],
      "line": 11,
      "id": "退出登录;退出登录;;1"
    },
    {
      "cells": [
        "我的信息",
        "退出登录",
        "退出登录",
        "确认退出",
        "登录"
      ],
      "line": 12,
      "id": "退出登录;退出登录;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 12,
  "name": "退出登录",
  "description": "",
  "id": "退出登录;退出登录;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"我的信息\"页,直到\"退出登录\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "我点击\"退出登录\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我点击\"确认退出\"",
  "matchedColumns": [
    3
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"登录\"出现",
  "matchedColumns": [
    4
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 3
    },
    {
      "val": "退出登录",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 95761311,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "退出登录",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 336652379,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "确认退出",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 1291019922,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 403487430,
  "status": "passed"
});
formatter.uri("Module02_G7TruckManagerMyInfo/Case01_G7TruckManagerAbout.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language:zh-CN"
    }
  ],
  "line": 2,
  "name": "关于页面",
  "description": "",
  "id": "关于页面",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 3,
  "name": "完成登录",
  "description": "",
  "id": "关于页面;完成登录",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "页面出现输入框,我输入\"\u003caccount\u003e\"和\"\u003cpassword\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 8,
  "name": "",
  "description": "",
  "id": "关于页面;完成登录;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "account",
        "password",
        "button",
        "title"
      ],
      "line": 9,
      "id": "关于页面;完成登录;;1"
    },
    {
      "cells": [
        "登录",
        "登录",
        "lifucai",
        "Qq123123",
        "登录",
        "手机管车"
      ],
      "line": 10,
      "id": "关于页面;完成登录;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 10,
  "name": "完成登录",
  "description": "",
  "id": "关于页面;完成登录;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 4,
  "name": "我在\"登录\"页,直到\"登录\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 5,
  "name": "页面出现输入框,我输入\"lifucai\"和\"Qq123123\"",
  "matchedColumns": [
    2,
    3
  ],
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我点击\"登录\"",
  "matchedColumns": [
    4
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"手机管车\"出现",
  "matchedColumns": [
    5
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 3
    },
    {
      "val": "登录",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 869227834,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "lifucai",
      "offset": 12
    },
    {
      "val": "Qq123123",
      "offset": 22
    }
  ],
  "location": "G7TruckManagerEditTextRelevantStepDefs.find_textFields(String,String)"
});
formatter.result({
  "duration": 31078595032,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 399440405,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 2878211259,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 12,
  "name": "进入我的",
  "description": "",
  "id": "关于页面;进入我的",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 14,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 15,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 16,
  "name": "",
  "description": "",
  "id": "关于页面;进入我的;",
  "rows": [
    {
      "cells": [
        "button",
        "title"
      ],
      "line": 17,
      "id": "关于页面;进入我的;;1"
    },
    {
      "cells": [
        "我的",
        "我的手机管车"
      ],
      "line": 18,
      "id": "关于页面;进入我的;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 18,
  "name": "进入我的",
  "description": "",
  "id": "关于页面;进入我的;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 14,
  "name": "我点击\"我的\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 15,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 339627963,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 815030981,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 20,
  "name": "滑动到页面直到关于出现",
  "description": "",
  "id": "关于页面;滑动到页面直到关于出现",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 21,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 22,
  "name": "向上滑动\u003cn\u003e次,直到\"\u003ctitle\u003e\"出现",
  "keyword": "当"
});
formatter.examples({
  "line": 23,
  "name": "",
  "description": "",
  "id": "关于页面;滑动到页面直到关于出现;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "n",
        "title"
      ],
      "line": 24,
      "id": "关于页面;滑动到页面直到关于出现;;1"
    },
    {
      "cells": [
        "我的手机管车",
        "我的手机管车",
        "1",
        "关于"
      ],
      "line": 25,
      "id": "关于页面;滑动到页面直到关于出现;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 25,
  "name": "滑动到页面直到关于出现",
  "description": "",
  "id": "关于页面;滑动到页面直到关于出现;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 21,
  "name": "我在\"我的手机管车\"页,直到\"我的手机管车\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 22,
  "name": "向上滑动1次,直到\"关于\"出现",
  "matchedColumns": [
    2,
    3
  ],
  "keyword": "当"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 3
    },
    {
      "val": "我的手机管车",
      "offset": 15
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 194876624,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "1",
      "offset": 4
    },
    {
      "val": "关于",
      "offset": 10
    }
  ],
  "location": "G7TruckManagerSwipeRelevantStepDefs.swipeToUp(int,String)"
});
formatter.result({
  "duration": 1034951058,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 27,
  "name": "进入关于页面",
  "description": "",
  "id": "关于页面;进入关于页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 28,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 29,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 30,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 31,
  "name": "",
  "description": "",
  "id": "关于页面;进入关于页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 32,
      "id": "关于页面;进入关于页面;;1"
    },
    {
      "cells": [
        "我的手机管车",
        "我的手机管车",
        "关于",
        "关于G7"
      ],
      "line": 33,
      "id": "关于页面;进入关于页面;;2"
    },
    {
      "cells": [
        "关于G7",
        "关于G7",
        "联系我们",
        "帮助"
      ],
      "line": 34,
      "id": "关于页面;进入关于页面;;3"
    },
    {
      "cells": [
        "帮助",
        "帮助",
        "取消",
        "关于G7"
      ],
      "line": 35,
      "id": "关于页面;进入关于页面;;4"
    },
    {
      "cells": [
        "关于G7",
        "关于G7",
        "联系我们",
        "帮助"
      ],
      "line": 36,
      "id": "关于页面;进入关于页面;;5"
    },
    {
      "cells": [
        "帮助",
        "帮助",
        "联系客服",
        "400 611 5656"
      ],
      "line": 37,
      "id": "关于页面;进入关于页面;;6"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 33,
  "name": "进入关于页面",
  "description": "",
  "id": "关于页面;进入关于页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 28,
  "name": "我在\"我的手机管车\"页,直到\"我的手机管车\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 29,
  "name": "我点击\"关于\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 30,
  "name": "我应该看到\"关于G7\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 3
    },
    {
      "val": "我的手机管车",
      "offset": 15
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 183182241,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "关于",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 695307923,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "关于G7",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 669741466,
  "status": "passed"
});
formatter.scenario({
  "line": 34,
  "name": "进入关于页面",
  "description": "",
  "id": "关于页面;进入关于页面;;3",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 28,
  "name": "我在\"关于G7\"页,直到\"关于G7\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 29,
  "name": "我点击\"联系我们\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 30,
  "name": "我应该看到\"帮助\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "关于G7",
      "offset": 3
    },
    {
      "val": "关于G7",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 557604183,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "联系我们",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 361872994,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "帮助",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 516011165,
  "status": "passed"
});
formatter.scenario({
  "line": 35,
  "name": "进入关于页面",
  "description": "",
  "id": "关于页面;进入关于页面;;4",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 28,
  "name": "我在\"帮助\"页,直到\"帮助\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 29,
  "name": "我点击\"取消\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 30,
  "name": "我应该看到\"关于G7\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "帮助",
      "offset": 3
    },
    {
      "val": "帮助",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 107724335,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "取消",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 3159651569,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "关于G7",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 16949402,
  "status": "passed"
});
formatter.scenario({
  "line": 36,
  "name": "进入关于页面",
  "description": "",
  "id": "关于页面;进入关于页面;;5",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 28,
  "name": "我在\"关于G7\"页,直到\"关于G7\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 29,
  "name": "我点击\"联系我们\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 30,
  "name": "我应该看到\"帮助\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "关于G7",
      "offset": 3
    },
    {
      "val": "关于G7",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 58200593,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "联系我们",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 330778860,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "帮助",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 547661770,
  "status": "passed"
});
formatter.scenario({
  "line": 37,
  "name": "进入关于页面",
  "description": "",
  "id": "关于页面;进入关于页面;;6",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 28,
  "name": "我在\"帮助\"页,直到\"帮助\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 29,
  "name": "我点击\"联系客服\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 30,
  "name": "我应该看到\"400 611 5656\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "帮助",
      "offset": 3
    },
    {
      "val": "帮助",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 96946100,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "联系客服",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 440911596,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "400 611 5656",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 425660614,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 42,
  "name": "从关于返回我的页面",
  "description": "",
  "id": "关于页面;从关于返回我的页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 43,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 44,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 45,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 46,
  "name": "",
  "description": "",
  "id": "关于页面;从关于返回我的页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "title"
      ],
      "line": 47,
      "id": "关于页面;从关于返回我的页面;;1"
    },
    {
      "cells": [
        "拨号页面",
        "400 611 5656",
        "关于G7"
      ],
      "line": 48,
      "id": "关于页面;从关于返回我的页面;;2"
    },
    {
      "cells": [
        "关于G7",
        "关于G7",
        "我的手机管车"
      ],
      "line": 49,
      "id": "关于页面;从关于返回我的页面;;3"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 48,
  "name": "从关于返回我的页面",
  "description": "",
  "id": "关于页面;从关于返回我的页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 43,
  "name": "我在\"拨号页面\"页,直到\"400 611 5656\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 44,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 45,
  "name": "我应该看到\"关于G7\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "拨号页面",
      "offset": 3
    },
    {
      "val": "400 611 5656",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 80006962,
  "status": "passed"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_backMenu()"
});
formatter.result({
  "duration": 58670046,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "关于G7",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 92820534,
  "status": "passed"
});
formatter.scenario({
  "line": 49,
  "name": "从关于返回我的页面",
  "description": "",
  "id": "关于页面;从关于返回我的页面;;3",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 43,
  "name": "我在\"关于G7\"页,直到\"关于G7\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 44,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 45,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "关于G7",
      "offset": 3
    },
    {
      "val": "关于G7",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 541296039,
  "status": "passed"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_backMenu()"
});
formatter.result({
  "duration": 34364687,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1032014744,
  "status": "passed"
});
formatter.uri("Module02_G7TruckManagerMyInfo/Case02_G7TruckManagerBuy.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language:zh-CN"
    }
  ],
  "line": 2,
  "name": "我要购买",
  "description": "",
  "id": "我要购买",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 4,
  "name": "切换到我的页面并进入G7商城页面",
  "description": "",
  "id": "我要购买;切换到我的页面并进入g7商城页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我等待\u003ctime\u003e秒",
  "keyword": "并且"
});
formatter.step({
  "line": 8,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 9,
  "name": "",
  "description": "",
  "id": "我要购买;切换到我的页面并进入g7商城页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "time",
        "title"
      ],
      "line": 10,
      "id": "我要购买;切换到我的页面并进入g7商城页面;;1"
    },
    {
      "cells": [
        "我的手机管车",
        "我的手机管车",
        "我要购买",
        "10000",
        "G7商城"
      ],
      "line": 11,
      "id": "我要购买;切换到我的页面并进入g7商城页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 11,
  "name": "切换到我的页面并进入G7商城页面",
  "description": "",
  "id": "我要购买;切换到我的页面并进入g7商城页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"我的手机管车\"页,直到\"我的手机管车\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我点击\"我要购买\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我等待10000秒",
  "matchedColumns": [
    3
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 8,
  "name": "我应该看到\"G7商城\"出现",
  "matchedColumns": [
    4
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 3
    },
    {
      "val": "我的手机管车",
      "offset": 15
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 396668757,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我要购买",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 736044589,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "10000",
      "offset": 3
    }
  ],
  "location": "G7TruckManagerOtherRelevantStepDefs.waitTime(int)"
});
formatter.result({
  "duration": 9999746531,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "G7商城",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 30862085,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 14,
  "name": "从商城返回我的页面",
  "description": "",
  "id": "我要购买;从商城返回我的页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 15,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 16,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 17,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 18,
  "name": "",
  "description": "",
  "id": "我要购买;从商城返回我的页面;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "title"
      ],
      "line": 19,
      "id": "我要购买;从商城返回我的页面;;1"
    },
    {
      "cells": [
        "G7商城",
        "G7商城",
        "我的手机管车"
      ],
      "line": 20,
      "id": "我要购买;从商城返回我的页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 20,
  "name": "从商城返回我的页面",
  "description": "",
  "id": "我要购买;从商城返回我的页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 15,
  "name": "我在\"G7商城\"页,直到\"G7商城\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 16,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 17,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    2
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "G7商城",
      "offset": 3
    },
    {
      "val": "G7商城",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 85521698,
  "status": "passed"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_backMenu()"
});
formatter.result({
  "duration": 29389465,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1138562768,
  "status": "passed"
});
formatter.uri("Module02_G7TruckManagerMyInfo/Case03_G7TruckManagerHelp.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language:zh-CN"
    }
  ],
  "line": 2,
  "name": "帮助",
  "description": "",
  "id": "帮助",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 4,
  "name": "切换到我的页面并进入帮助页面查看常见问题",
  "description": "",
  "id": "帮助;切换到我的页面并进入帮助页面查看常见问题",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 8,
  "name": "",
  "description": "",
  "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 9,
      "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;;1"
    },
    {
      "cells": [
        "我的手机管车",
        "我的手机管车",
        "帮助",
        "帮助"
      ],
      "line": 10,
      "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;;2"
    },
    {
      "cells": [
        "帮助",
        "常见问题",
        "常见问题",
        "常见问题"
      ],
      "line": 11,
      "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;;3"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 10,
  "name": "切换到我的页面并进入帮助页面查看常见问题",
  "description": "",
  "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"我的手机管车\"页,直到\"我的手机管车\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我点击\"帮助\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"帮助\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 3
    },
    {
      "val": "我的手机管车",
      "offset": 15
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 370360190,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "帮助",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 588962495,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "帮助",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 624585156,
  "status": "passed"
});
formatter.scenario({
  "line": 11,
  "name": "切换到我的页面并进入帮助页面查看常见问题",
  "description": "",
  "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;;3",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我在\"帮助\"页,直到\"常见问题\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 6,
  "name": "我点击\"常见问题\"",
  "matchedColumns": [
    2
  ],
  "keyword": "当"
});
formatter.step({
  "line": 7,
  "name": "我应该看到\"常见问题\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "帮助",
      "offset": 3
    },
    {
      "val": "常见问题",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 123954384,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "常见问题",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 557770633,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "常见问题",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1392317389,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 14,
  "name": "切换到我的页面并进入帮助页面查看常见问题",
  "description": "",
  "id": "帮助;切换到我的页面并进入帮助页面查看常见问题",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 15,
  "name": "我在\"\u003cpage\u003e\"页,直到\"\u003ckeyword\u003e\"出现",
  "keyword": "假设"
});
formatter.step({
  "line": 16,
  "name": "我切换到WebView",
  "keyword": "当"
});
formatter.step({
  "line": 17,
  "name": "我点击WebView\"\u003cbutton\u003e\"",
  "keyword": "并且"
});
formatter.step({
  "line": 18,
  "name": "我应该看到WebView\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 19,
  "name": "",
  "description": "",
  "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;",
  "rows": [
    {
      "cells": [
        "page",
        "keyword",
        "button",
        "title"
      ],
      "line": 20,
      "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;;1"
    },
    {
      "cells": [
        "常见问题",
        "常见问题",
        "忘记密码",
        "忘记密码"
      ],
      "line": 21,
      "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 21,
  "name": "切换到我的页面并进入帮助页面查看常见问题",
  "description": "",
  "id": "帮助;切换到我的页面并进入帮助页面查看常见问题;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 15,
  "name": "我在\"常见问题\"页,直到\"常见问题\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "假设"
});
formatter.step({
  "line": 16,
  "name": "我切换到WebView",
  "keyword": "当"
});
formatter.step({
  "line": 17,
  "name": "我点击WebView\"忘记密码\"",
  "matchedColumns": [
    2
  ],
  "keyword": "并且"
});
formatter.step({
  "line": 18,
  "name": "我应该看到WebView\"忘记密码\"出现",
  "matchedColumns": [
    3
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "常见问题",
      "offset": 3
    },
    {
      "val": "常见问题",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerPageRelevantStepDefs.which_page_on(String,String)"
});
formatter.result({
  "duration": 190254384,
  "status": "passed"
});
formatter.match({
  "location": "G7TruckManagerWebViewNativeRelevantStepDefs.change_webview()"
});
formatter.result({
  "duration": 4418529567,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "忘记密码",
      "offset": 11
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click_webviwe(String)"
});
formatter.result({
  "duration": 336985280,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "忘记密码",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see_webview(String)"
});
formatter.result({
  "duration": 83749645,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 23,
  "name": "从常见问题返回帮助页面",
  "description": "",
  "id": "帮助;从常见问题返回帮助页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 24,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 25,
  "name": "我应该看到WebView\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 26,
  "name": "",
  "description": "",
  "id": "帮助;从常见问题返回帮助页面;",
  "rows": [
    {
      "cells": [
        "title"
      ],
      "line": 27,
      "id": "帮助;从常见问题返回帮助页面;;1"
    },
    {
      "cells": [
        "基础账户设置"
      ],
      "line": 28,
      "id": "帮助;从常见问题返回帮助页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 28,
  "name": "从常见问题返回帮助页面",
  "description": "",
  "id": "帮助;从常见问题返回帮助页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 24,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 25,
  "name": "我应该看到WebView\"基础账户设置\"出现",
  "matchedColumns": [
    0
  ],
  "keyword": "那么"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_backMenu()"
});
formatter.result({
  "duration": 44210264,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "基础账户设置",
      "offset": 13
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see_webview(String)"
});
formatter.result({
  "duration": 113310471,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 30,
  "name": "从常见问题返回帮助页面",
  "description": "",
  "id": "帮助;从常见问题返回帮助页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 31,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 32,
  "name": "我切换到Native",
  "keyword": "并且"
});
formatter.step({
  "line": 33,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 34,
  "name": "",
  "description": "",
  "id": "帮助;从常见问题返回帮助页面;",
  "rows": [
    {
      "cells": [
        "title"
      ],
      "line": 35,
      "id": "帮助;从常见问题返回帮助页面;;1"
    },
    {
      "cells": [
        "使用说明"
      ],
      "line": 36,
      "id": "帮助;从常见问题返回帮助页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 36,
  "name": "从常见问题返回帮助页面",
  "description": "",
  "id": "帮助;从常见问题返回帮助页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 31,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 32,
  "name": "我切换到Native",
  "keyword": "并且"
});
formatter.step({
  "line": 33,
  "name": "我应该看到\"使用说明\"出现",
  "matchedColumns": [
    0
  ],
  "keyword": "那么"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_backMenu()"
});
formatter.result({
  "duration": 40709446,
  "status": "passed"
});
formatter.match({
  "location": "G7TruckManagerWebViewNativeRelevantStepDefs.change_native()"
});
formatter.result({
  "duration": 372462018,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "使用说明",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 221869735,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 38,
  "name": "在使用说明页面滑动查看说明",
  "description": "",
  "id": "帮助;在使用说明页面滑动查看说明",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 39,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 40,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 41,
  "name": "",
  "description": "",
  "id": "帮助;在使用说明页面滑动查看说明;",
  "rows": [
    {
      "cells": [
        "button",
        "title"
      ],
      "line": 42,
      "id": "帮助;在使用说明页面滑动查看说明;;1"
    },
    {
      "cells": [
        "使用说明",
        "使用说明"
      ],
      "line": 43,
      "id": "帮助;在使用说明页面滑动查看说明;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 43,
  "name": "在使用说明页面滑动查看说明",
  "description": "",
  "id": "帮助;在使用说明页面滑动查看说明;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 39,
  "name": "我点击\"使用说明\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 40,
  "name": "我应该看到\"使用说明\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "使用说明",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 605358549,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "使用说明",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1661060599,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 45,
  "name": "从使用返回帮助页面",
  "description": "",
  "id": "帮助;从使用返回帮助页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 46,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 47,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 48,
  "name": "",
  "description": "",
  "id": "帮助;从使用返回帮助页面;",
  "rows": [
    {
      "cells": [
        "title"
      ],
      "line": 49,
      "id": "帮助;从使用返回帮助页面;;1"
    },
    {
      "cells": [
        "常见问题"
      ],
      "line": 50,
      "id": "帮助;从使用返回帮助页面;;2"
    },
    {
      "cells": [
        "我的手机管车"
      ],
      "line": 51,
      "id": "帮助;从使用返回帮助页面;;3"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 50,
  "name": "从使用返回帮助页面",
  "description": "",
  "id": "帮助;从使用返回帮助页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 46,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 47,
  "name": "我应该看到\"常见问题\"出现",
  "matchedColumns": [
    0
  ],
  "keyword": "那么"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_backMenu()"
});
formatter.result({
  "duration": 33329391,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "常见问题",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 707436950,
  "status": "passed"
});
formatter.scenario({
  "line": 51,
  "name": "从使用返回帮助页面",
  "description": "",
  "id": "帮助;从使用返回帮助页面;;3",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 46,
  "name": "我点击back键",
  "keyword": "当"
});
formatter.step({
  "line": 47,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    0
  ],
  "keyword": "那么"
});
formatter.match({
  "location": "G7TruckManagerClickRelevantStepDefs.click_backMenu()"
});
formatter.result({
  "duration": 28487598,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1181311122,
  "status": "passed"
});
formatter.uri("Module02_G7TruckManagerMyInfo/Case04_G7TruckManagerMobile.feature");
formatter.feature({
  "comments": [
    {
      "line": 1,
      "value": "#language:zh-CN"
    }
  ],
  "line": 2,
  "name": "联系客服",
  "description": "",
  "id": "联系客服",
  "keyword": "功能"
});
formatter.scenarioOutline({
  "line": 4,
  "name": "切换到我的页面并进入联系客服页面",
  "description": "",
  "id": "联系客服;切换到我的页面并进入联系客服页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 7,
  "name": "",
  "description": "",
  "id": "联系客服;切换到我的页面并进入联系客服页面;",
  "rows": [
    {
      "cells": [
        "button",
        "title"
      ],
      "line": 8,
      "id": "联系客服;切换到我的页面并进入联系客服页面;;1"
    },
    {
      "cells": [
        "联系客服",
        "在线客服"
      ],
      "line": 9,
      "id": "联系客服;切换到我的页面并进入联系客服页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 9,
  "name": "切换到我的页面并进入联系客服页面",
  "description": "",
  "id": "联系客服;切换到我的页面并进入联系客服页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 5,
  "name": "我点击\"联系客服\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 6,
  "name": "我应该看到\"在线客服\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "联系客服",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 626184064,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "在线客服",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 2605347393,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 11,
  "name": "从联系客服返回我的页面",
  "description": "",
  "id": "联系客服;从联系客服返回我的页面",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 12,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 13,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 14,
  "name": "",
  "description": "",
  "id": "联系客服;从联系客服返回我的页面;",
  "rows": [
    {
      "cells": [
        "button",
        "title"
      ],
      "line": 15,
      "id": "联系客服;从联系客服返回我的页面;;1"
    },
    {
      "cells": [
        "在线客服",
        "我的手机管车"
      ],
      "line": 16,
      "id": "联系客服;从联系客服返回我的页面;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 16,
  "name": "从联系客服返回我的页面",
  "description": "",
  "id": "联系客服;从联系客服返回我的页面;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 12,
  "name": "我点击\"在线客服\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 13,
  "name": "我应该看到\"我的手机管车\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "在线客服",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 277522698,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的手机管车",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 1130464255,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 18,
  "name": "滑动到页面直到我的信息出现",
  "description": "",
  "id": "联系客服;滑动到页面直到我的信息出现",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 19,
  "name": "向下滑动\u003cn\u003e次,直到\"\u003ctitle\u003e\"出现",
  "keyword": "当"
});
formatter.examples({
  "line": 20,
  "name": "",
  "description": "",
  "id": "联系客服;滑动到页面直到我的信息出现;",
  "rows": [
    {
      "cells": [
        "n",
        "title"
      ],
      "line": 21,
      "id": "联系客服;滑动到页面直到我的信息出现;;1"
    },
    {
      "cells": [
        "1",
        "我的信息"
      ],
      "line": 22,
      "id": "联系客服;滑动到页面直到我的信息出现;;2"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 22,
  "name": "滑动到页面直到我的信息出现",
  "description": "",
  "id": "联系客服;滑动到页面直到我的信息出现;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 19,
  "name": "向下滑动1次,直到\"我的信息\"出现",
  "matchedColumns": [
    0,
    1
  ],
  "keyword": "当"
});
formatter.match({
  "arguments": [
    {
      "val": "1",
      "offset": 4
    },
    {
      "val": "我的信息",
      "offset": 10
    }
  ],
  "location": "G7TruckManagerSwipeRelevantStepDefs.swipeToDown(int,String)"
});
formatter.result({
  "duration": 993538771,
  "status": "passed"
});
formatter.scenarioOutline({
  "line": 23,
  "name": "退出登录",
  "description": "",
  "id": "联系客服;退出登录",
  "type": "scenario_outline",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 24,
  "name": "我点击\"\u003cbutton\u003e\"",
  "keyword": "当"
});
formatter.step({
  "line": 25,
  "name": "我应该看到\"\u003ctitle\u003e\"出现",
  "keyword": "那么"
});
formatter.examples({
  "line": 26,
  "name": "",
  "description": "",
  "id": "联系客服;退出登录;",
  "rows": [
    {
      "cells": [
        "button",
        "title"
      ],
      "line": 27,
      "id": "联系客服;退出登录;;1"
    },
    {
      "cells": [
        "我的信息",
        "我的信息"
      ],
      "line": 28,
      "id": "联系客服;退出登录;;2"
    },
    {
      "cells": [
        "退出登录",
        "确认退出"
      ],
      "line": 29,
      "id": "联系客服;退出登录;;3"
    },
    {
      "cells": [
        "确认退出",
        "登录"
      ],
      "line": 30,
      "id": "联系客服;退出登录;;4"
    }
  ],
  "keyword": "例子"
});
formatter.scenario({
  "line": 28,
  "name": "退出登录",
  "description": "",
  "id": "联系客服;退出登录;;2",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 24,
  "name": "我点击\"我的信息\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 25,
  "name": "我应该看到\"我的信息\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 481221649,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "我的信息",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 663919264,
  "status": "passed"
});
formatter.scenario({
  "line": 29,
  "name": "退出登录",
  "description": "",
  "id": "联系客服;退出登录;;3",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 24,
  "name": "我点击\"退出登录\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 25,
  "name": "我应该看到\"确认退出\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "退出登录",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 381233475,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "确认退出",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 532303243,
  "status": "passed"
});
formatter.scenario({
  "line": 30,
  "name": "退出登录",
  "description": "",
  "id": "联系客服;退出登录;;4",
  "type": "scenario",
  "keyword": "场景大纲"
});
formatter.step({
  "line": 24,
  "name": "我点击\"确认退出\"",
  "matchedColumns": [
    0
  ],
  "keyword": "当"
});
formatter.step({
  "line": 25,
  "name": "我应该看到\"登录\"出现",
  "matchedColumns": [
    1
  ],
  "keyword": "那么"
});
formatter.match({
  "arguments": [
    {
      "val": "确认退出",
      "offset": 4
    }
  ],
  "location": "G7TruckManagerClickRelevantStepDefs.i_click(String)"
});
formatter.result({
  "duration": 1052737175,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "登录",
      "offset": 6
    }
  ],
  "location": "G7TruckManagerExpectResultRelevantStepDefs.i_will_see(String)"
});
formatter.result({
  "duration": 366608580,
  "status": "passed"
});
});