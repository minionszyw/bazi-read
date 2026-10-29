# 八字静态排盘

规则：{"time_basis": "apparent", "year_boundary": "lichun", "day_boundary": "midnight", "late_zi": "same_day"}

|柱|干支|十神|藏干（十神）|纳音|旬空|十二长生|
|---|---|---|---|---|---|---|
|year|庚午|偏印|丁（正财）、己（正官）|路旁土|戌亥|沐浴|
|month|辛巳|正印|丙（偏财）、戊（七杀）、庚（偏印）|白蜡金|申酉|死|
|day|壬午|日主|丁（正财）、己（正官）|杨柳木|申酉|胎|
|hour|丁未|正财|己（正官）、丁（正财）、乙（伤官）|天河水|寅卯|冠带|

## 时间与节令

```json
{
  "time": {
    "civil": "1990-05-17T14:30:00+09:00",
    "utc": "1990-05-17T05:30:00+00:00",
    "mean_solar": "1990-05-17T13:15:37.268400",
    "apparent_solar": "1990-05-17T13:19:16.658587",
    "selected_clock": "1990-05-17T13:19:16.658587",
    "longitude": 116.405285,
    "longitude_source": "explicit",
    "equation_minutes": 3.6565031112568898,
    "longitude_from_utc_minutes": 465.62114,
    "lunar": {
      "year": 1990,
      "month": 4,
      "day": 23,
      "is_leap_month": false
    }
  },
  "season": {
    "previous_term": {
      "name": "立夏",
      "utc": "1990-05-05T18:35:26.267395+00:00",
      "distance_seconds": -989673.732605
    },
    "next_term": {
      "name": "小满",
      "utc": "1990-05-21T07:37:23.116379+00:00",
      "distance_seconds": 353243.116379
    },
    "previous_jie": {
      "name": "立夏",
      "utc": "1990-05-05T18:35:26.267395+00:00",
      "distance_seconds": -989673.732605
    },
    "next_jie": {
      "name": "芒种",
      "utc": "1990-06-05T22:46:17.673340+00:00",
      "distance_seconds": 1703777.67334
    },
    "elapsed_since_jie_seconds": 989673.732605
  }
}
```

## 大运

起运：1996-12-13T23:05:20.800800+08:00；折算年龄：{'years': 6, 'months': 6, 'days': 26, 'seconds': 30920.80079999566}

- 1996-12-13T23:05:20.800800+08:00：壬午
- 2006-12-13T23:05:20.800800+08:00：癸未
- 2016-12-13T23:05:20.800800+08:00：甲申
- 2026-12-13T23:05:20.800800+08:00：乙酉
- 2036-12-13T23:05:20.800800+08:00：丙戌
- 2046-12-13T23:05:20.800800+08:00：丁亥
- 2056-12-13T23:05:20.800800+08:00：戊子
- 2066-12-13T23:05:20.800800+08:00：己丑
- 2076-12-13T23:05:20.800800+08:00：庚寅
- 2086-12-13T23:05:20.800800+08:00：辛卯

## 干支关系

```json
[
  {
    "type": "天干同类",
    "positions": [
      "year",
      "month"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "自刑",
    "positions": [
      "year",
      "day"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "天干前生后",
    "positions": [
      "year",
      "day"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "六合",
    "positions": [
      "year",
      "hour"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "天干后克前",
    "positions": [
      "year",
      "hour"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "天干前生后",
    "positions": [
      "month",
      "day"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "天干后克前",
    "positions": [
      "month",
      "hour"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "天干五合",
    "positions": [
      "day",
      "hour"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "六合",
    "positions": [
      "day",
      "hour"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "天干前克后",
    "positions": [
      "day",
      "hour"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "三会",
    "positions": [
      "year",
      "month",
      "hour"
    ],
    "rule_id": "REL-01"
  },
  {
    "type": "三会",
    "positions": [
      "month",
      "day",
      "hour"
    ],
    "rule_id": "REL-01"
  }
]
```

## 辅助表

```json
{
  "fetal_month_formula": {
    "ganzhi": "壬申",
    "rule_id": "AUX-01"
  },
  "fetal_300_days": {
    "date": "1989-07-21",
    "ganzhi": "壬午",
    "rule_id": "AUX-02"
  },
  "life_palace": {
    "ganzhi": "辛巳",
    "month_basis": "civil_date_chinese_lunar_month",
    "rule_id": "AUX-03"
  },
  "stars": [
    {
      "name": "天乙贵人",
      "position": "month",
      "reference": "day.stem",
      "targets": "卯巳",
      "rule_id": "STAR-天乙贵人",
      "status": "traditional_table_pending_scan_collation"
    },
    {
      "name": "月德",
      "position": "year",
      "reference": "month.branch",
      "targets": "庚",
      "rule_id": "STAR-月德",
      "status": "traditional_table_pending_scan_collation"
    },
    {
      "name": "天德",
      "position": "month",
      "reference": "month.branch",
      "targets": "辛",
      "rule_id": "STAR-天德",
      "status": "traditional_table_pending_scan_collation"
    },
    {
      "name": "将星",
      "position": "year",
      "reference": "year.branch",
      "targets": "午",
      "rule_id": "STAR-将星",
      "status": "traditional_table_pending_scan_collation"
    },
    {
      "name": "将星",
      "position": "day",
      "reference": "year.branch",
      "targets": "午",
      "rule_id": "STAR-将星",
      "status": "traditional_table_pending_scan_collation"
    },
    {
      "name": "将星",
      "position": "year",
      "reference": "day.branch",
      "targets": "午",
      "rule_id": "STAR-将星",
      "status": "traditional_table_pending_scan_collation"
    },
    {
      "name": "将星",
      "position": "day",
      "reference": "day.branch",
      "targets": "午",
      "rule_id": "STAR-将星",
      "status": "traditional_table_pending_scan_collation"
    }
  ]
}
```

## 流年

```json
[
  {
    "year": 1990,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "庚午",
      "stem_element": "金",
      "stem_polarity": "阳",
      "stem_ten_god": "偏印",
      "hidden": [
        {
          "stem": "丁",
          "ten_god": "正财"
        },
        {
          "stem": "己",
          "ten_god": "正官"
        }
      ],
      "nayin": "路旁土",
      "void": "戌亥",
      "growth_stage": "沐浴"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1991,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "辛未",
      "stem_element": "金",
      "stem_polarity": "阴",
      "stem_ten_god": "正印",
      "hidden": [
        {
          "stem": "己",
          "ten_god": "正官"
        },
        {
          "stem": "丁",
          "ten_god": "正财"
        },
        {
          "stem": "乙",
          "ten_god": "伤官"
        }
      ],
      "nayin": "路旁土",
      "void": "戌亥",
      "growth_stage": "衰"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1992,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "壬申",
      "stem_element": "水",
      "stem_polarity": "阳",
      "stem_ten_god": "比肩",
      "hidden": [
        {
          "stem": "庚",
          "ten_god": "偏印"
        },
        {
          "stem": "壬",
          "ten_god": "比肩"
        },
        {
          "stem": "戊",
          "ten_god": "七杀"
        }
      ],
      "nayin": "剑锋金",
      "void": "戌亥",
      "growth_stage": "长生"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六破",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "刑",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1993,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "癸酉",
      "stem_element": "水",
      "stem_polarity": "阴",
      "stem_ten_god": "劫财",
      "hidden": [
        {
          "stem": "辛",
          "ten_god": "正印"
        }
      ],
      "nayin": "剑锋金",
      "void": "戌亥",
      "growth_stage": "病"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1994,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "甲戌",
      "stem_element": "木",
      "stem_polarity": "阳",
      "stem_ten_god": "食神",
      "hidden": [
        {
          "stem": "戊",
          "ten_god": "七杀"
        },
        {
          "stem": "辛",
          "ten_god": "正印"
        },
        {
          "stem": "丁",
          "ten_god": "正财"
        }
      ],
      "nayin": "山头火",
      "void": "申酉",
      "growth_stage": "养"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六破",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "刑",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1995,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "乙亥",
      "stem_element": "木",
      "stem_polarity": "阴",
      "stem_ten_god": "伤官",
      "hidden": [
        {
          "stem": "壬",
          "ten_god": "比肩"
        },
        {
          "stem": "甲",
          "ten_god": "食神"
        }
      ],
      "nayin": "山头火",
      "void": "申酉",
      "growth_stage": "死"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六冲",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1996,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "丙子",
      "stem_element": "火",
      "stem_polarity": "阳",
      "stem_ten_god": "偏财",
      "hidden": [
        {
          "stem": "癸",
          "ten_god": "劫财"
        }
      ],
      "nayin": "涧下水",
      "void": "申酉",
      "growth_stage": "胎"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六冲",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六冲",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六害",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1997,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "丁丑",
      "stem_element": "火",
      "stem_polarity": "阴",
      "stem_ten_god": "正财",
      "hidden": [
        {
          "stem": "己",
          "ten_god": "正官"
        },
        {
          "stem": "癸",
          "ten_god": "劫财"
        },
        {
          "stem": "辛",
          "ten_god": "正印"
        }
      ],
      "nayin": "涧下水",
      "void": "申酉",
      "growth_stage": "墓"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六害",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六害",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六冲",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "刑",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1998,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "戊寅",
      "stem_element": "土",
      "stem_polarity": "阳",
      "stem_ten_god": "七杀",
      "hidden": [
        {
          "stem": "甲",
          "ten_god": "食神"
        },
        {
          "stem": "丙",
          "ten_god": "偏财"
        },
        {
          "stem": "戊",
          "ten_god": "七杀"
        }
      ],
      "nayin": "城头土",
      "void": "申酉",
      "growth_stage": "长生"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六害",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "刑",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "year": 1999,
    "year_boundary": "lichun",
    "pillar": {
      "ganzhi": "己卯",
      "stem_element": "土",
      "stem_polarity": "阴",
      "stem_ten_god": "正官",
      "hidden": [
        {
          "stem": "乙",
          "ten_god": "伤官"
        }
      ],
      "nayin": "城头土",
      "void": "申酉",
      "growth_stage": "病"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六破",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "year",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "month",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六破",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "day",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "hour",
          "annual"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  }
]
```

## 流月

```json
[
  {
    "start": "2026-02-03T20:01:51.392784+00:00",
    "end": "2026-03-05T13:58:42.759247+00:00",
    "pillar": {
      "ganzhi": "庚寅",
      "stem_element": "金",
      "stem_polarity": "阳",
      "stem_ten_god": "偏印",
      "hidden": [
        {
          "stem": "甲",
          "ten_god": "食神"
        },
        {
          "stem": "丙",
          "ten_god": "偏财"
        },
        {
          "stem": "戊",
          "ten_god": "七杀"
        }
      ],
      "nayin": "松柏木",
      "void": "午未",
      "growth_stage": "绝"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六害",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "刑",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-03-05T13:58:42.759247+00:00",
    "end": "2026-04-04T18:39:42.950821+00:00",
    "pillar": {
      "ganzhi": "辛卯",
      "stem_element": "金",
      "stem_polarity": "阴",
      "stem_ten_god": "正印",
      "hidden": [
        {
          "stem": "乙",
          "ten_god": "伤官"
        }
      ],
      "nayin": "松柏木",
      "void": "午未",
      "growth_stage": "绝"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六破",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六破",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-04-04T18:39:42.950821+00:00",
    "end": "2026-05-05T11:48:26.611633+00:00",
    "pillar": {
      "ganzhi": "壬辰",
      "stem_element": "水",
      "stem_polarity": "阳",
      "stem_ten_god": "比肩",
      "hidden": [
        {
          "stem": "戊",
          "ten_god": "七杀"
        },
        {
          "stem": "乙",
          "ten_god": "伤官"
        },
        {
          "stem": "癸",
          "ten_god": "劫财"
        }
      ],
      "nayin": "长流水",
      "void": "午未",
      "growth_stage": "墓"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-05-05T11:48:26.611633+00:00",
    "end": "2026-06-05T15:48:03.705139+00:00",
    "pillar": {
      "ganzhi": "癸巳",
      "stem_element": "水",
      "stem_polarity": "阴",
      "stem_ten_god": "劫财",
      "hidden": [
        {
          "stem": "丙",
          "ten_god": "偏财"
        },
        {
          "stem": "戊",
          "ten_god": "七杀"
        },
        {
          "stem": "庚",
          "ten_god": "偏印"
        }
      ],
      "nayin": "长流水",
      "void": "午未",
      "growth_stage": "胎"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "day",
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-06-05T15:48:03.705139+00:00",
    "end": "2026-07-07T01:56:39.626541+00:00",
    "pillar": {
      "ganzhi": "甲午",
      "stem_element": "木",
      "stem_polarity": "阳",
      "stem_ten_god": "食神",
      "hidden": [
        {
          "stem": "丁",
          "ten_god": "正财"
        },
        {
          "stem": "己",
          "ten_god": "正官"
        }
      ],
      "nayin": "沙中金",
      "void": "辰巳",
      "growth_stage": "死"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-07-07T01:56:39.626541+00:00",
    "end": "2026-08-07T11:42:25.635223+00:00",
    "pillar": {
      "ganzhi": "乙未",
      "stem_element": "木",
      "stem_polarity": "阴",
      "stem_ten_god": "伤官",
      "hidden": [
        {
          "stem": "己",
          "ten_god": "正官"
        },
        {
          "stem": "丁",
          "ten_god": "正财"
        },
        {
          "stem": "乙",
          "ten_god": "伤官"
        }
      ],
      "nayin": "沙中金",
      "void": "辰巳",
      "growth_stage": "养"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-08-07T11:42:25.635223+00:00",
    "end": "2026-09-07T14:40:58.534241+00:00",
    "pillar": {
      "ganzhi": "丙申",
      "stem_element": "火",
      "stem_polarity": "阳",
      "stem_ten_god": "偏财",
      "hidden": [
        {
          "stem": "庚",
          "ten_god": "偏印"
        },
        {
          "stem": "壬",
          "ten_god": "比肩"
        },
        {
          "stem": "戊",
          "ten_god": "七杀"
        }
      ],
      "nayin": "山下火",
      "void": "辰巳",
      "growth_stage": "病"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六破",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "刑",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-09-07T14:40:58.534241+00:00",
    "end": "2026-10-08T06:28:59.417267+00:00",
    "pillar": {
      "ganzhi": "丁酉",
      "stem_element": "火",
      "stem_polarity": "阴",
      "stem_ten_god": "正财",
      "hidden": [
        {
          "stem": "辛",
          "ten_god": "正印"
        }
      ],
      "nayin": "山下火",
      "void": "辰巳",
      "growth_stage": "长生"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-10-08T06:28:59.417267+00:00",
    "end": "2026-11-07T09:51:46.301880+00:00",
    "pillar": {
      "ganzhi": "戊戌",
      "stem_element": "土",
      "stem_polarity": "阳",
      "stem_ten_god": "七杀",
      "hidden": [
        {
          "stem": "戊",
          "ten_god": "七杀"
        },
        {
          "stem": "辛",
          "ten_god": "正印"
        },
        {
          "stem": "丁",
          "ten_god": "正财"
        }
      ],
      "nayin": "平地木",
      "void": "辰巳",
      "growth_stage": "墓"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六破",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "刑",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-11-07T09:51:46.301880+00:00",
    "end": "2026-12-07T02:52:13.575439+00:00",
    "pillar": {
      "ganzhi": "己亥",
      "stem_element": "土",
      "stem_polarity": "阴",
      "stem_ten_god": "正官",
      "hidden": [
        {
          "stem": "壬",
          "ten_god": "比肩"
        },
        {
          "stem": "甲",
          "ten_god": "食神"
        }
      ],
      "nayin": "平地木",
      "void": "辰巳",
      "growth_stage": "胎"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六冲",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2026-12-07T02:52:13.575439+00:00",
    "end": "2027-01-05T14:09:39.384613+00:00",
    "pillar": {
      "ganzhi": "庚子",
      "stem_element": "金",
      "stem_polarity": "阳",
      "stem_ten_god": "偏印",
      "hidden": [
        {
          "stem": "癸",
          "ten_god": "劫财"
        }
      ],
      "nayin": "壁上土",
      "void": "辰巳",
      "growth_stage": "死"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六冲",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六冲",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六害",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  },
  {
    "start": "2027-01-05T14:09:39.384613+00:00",
    "end": "2027-02-04T01:45:59.933853+00:00",
    "pillar": {
      "ganzhi": "辛丑",
      "stem_element": "金",
      "stem_polarity": "阴",
      "stem_ten_god": "正印",
      "hidden": [
        {
          "stem": "己",
          "ten_god": "正官"
        },
        {
          "stem": "癸",
          "ten_god": "劫财"
        },
        {
          "stem": "辛",
          "ten_god": "正印"
        }
      ],
      "nayin": "壁上土",
      "void": "辰巳",
      "growth_stage": "养"
    },
    "relations": [
      {
        "type": "天干同类",
        "positions": [
          "year",
          "month"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "自刑",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "year",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "year",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六害",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "year",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前生后",
        "positions": [
          "month",
          "day"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后克前",
        "positions": [
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干同类",
        "positions": [
          "month",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干五合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六合",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六害",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干后生前",
        "positions": [
          "day",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "六冲",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "刑",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "天干前克后",
        "positions": [
          "hour",
          "monthly"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "year",
          "month",
          "hour"
        ],
        "rule_id": "REL-01"
      },
      {
        "type": "三会",
        "positions": [
          "month",
          "day",
          "hour"
        ],
        "rule_id": "REL-01"
      }
    ]
  }
]
```

## 提示

```json
[]
```

