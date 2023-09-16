from src.util import open_list, sort_execut, sort_list, five_last, time, from_out, to_in

def test_open_list():
    q = open_list('../operations.json')
    assert isinstance (q, list)


def test_sort_execut():
    assert sort_execut([
  {
    "id": 441945886,
    "state": "EXECUTED",
    },
  {
    "id": 41428829,
    "state": "EXECUTED",
    },
  {
    "id": 939719570,
    "state": "EXECUTED",
    },
  {
    "id": 587085106,
    "state": "EXECUTED",
   },
  {
    "id": 142264268,
    "state": "EXECUTED",
   },
  {
    "id": 873106923,
    "state": "EXECUTED",
    },
  {
    "id": 214024827,
    "state": "EXECUTED",
   },
  {
    "id": 522357576,
    "state": "EXECUTED",
    },
  {
    "id": 895315941,
    "state": "EXECUTED",
   },
  {
    "id": 596171168,
    "state": "EXECUTED",
   },
  {
    "id": 716496732,
    "state": "EXECUTED",
   },
  {
    "id": 863064926,
    "state": "EXECUTED",
   },
  {
    "id": 594226727,
    "state": "CANCELED",
   }]) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    },
  {
    "id": 41428829,
    "state": "EXECUTED",
    },
  {
    "id": 939719570,
    "state": "EXECUTED",
    },
  {
    "id": 587085106,
    "state": "EXECUTED",
   },
  {
    "id": 142264268,
    "state": "EXECUTED",
   },
  {
    "id": 873106923,
    "state": "EXECUTED",
    },
  {
    "id": 214024827,
    "state": "EXECUTED",
   },
  {
    "id": 522357576,
    "state": "EXECUTED",
    },
  {
    "id": 895315941,
    "state": "EXECUTED",
   },
  {
    "id": 596171168,
    "state": "EXECUTED",
   },
  {
    "id": 716496732,
    "state": "EXECUTED",
   },
  {
    "id": 863064926,
    "state": "EXECUTED",
   }]

def test_sort_list():
    assert sort_list([
    {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246"
      },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
      },
  {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
      },
  {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",

  },
  {
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
      },
  {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",

  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",

  }]) == [
  {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
  },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
  },
  {
    "id": 214024827,
    "state": "EXECUTED",
     "date": "2018-12-20T16:43:26.929246"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",

  },

  {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
      },
  {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",

  },
  {
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
      }

 ]

def test_five_last():
    assert five_last([
  {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
  },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
  },
  {
    "id": 214024827,
    "state": "EXECUTED",
     "date": "2018-12-20T16:43:26.929246"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",

  },

  {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
      },
  {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",

  },
  {
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
      }

 ]) == [
  {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
  },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
  },
  {
    "id": 214024827,
    "state": "EXECUTED",
     "date": "2018-12-20T16:43:26.929246"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",

  },

  {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
      }

 ]


def test_time():
  assert time("2019-07-12T20:41:47.882230") == '12.07.2019'

def test_from_out_card():
    assert from_out({"description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  }) == "Visa Classic 6831 98** **** 7658"


def test_from_out_schet():
  assert from_out({"description": "Перевод организации",
    "from": "Счет 27248529432547658655",
    "to": "Счет 97584898735659638967"
                   }) == "Счет **** **** **** **** 8655"

def test_from_out_open_schet():
  assert from_out({"description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
                   }) == ""

def test_to_in_card():
    assert to_in({"description": "Перевод с карты на карту",
                     "from": "Visa Classic 6831982476737658",
                     "to": "Visa Platinum 8990922113665229"
                     }) == "Visa Platinum 8990 92** **** 5229"


def test_to_in_schet():
  assert to_in({"description": "Перевод организации",
                   "from": "Счет 27248529432547658655",
                   "to": "Счет 97584898735659638967"
                   }) == "Счет **** **** **** **** 8967"

