import sys
import inspect
from iapws import IAPWS97, IAPWS95
from yangke.performance.iapws97 import get_p_by_ht, get_h_by_pt, get_t_by_hp


class TestPoint:
    """
    机组测点的流量及热力参数
    """

    def __init__(self):
        self.p: float = -1
        self.t: float = -1
        self.h: float = -1
        self.mass_flow = -1  # 质量流量
        self.available: bool = False  # 参数是否可用，仅当所有参数都可用时为True
        self.necessary: bool = True  # 参数是否必要

    def init_state(self):
        pass

    def set_state_by_name_and_value_list(self, test_point_name_list, value_list):
        """
        根据试验测点中已有数据更新测点中水或水蒸汽气的状态数据

        :param test_point_name_list:
        :param value_list:
        :return:
        """
        t_n = 0
        p_n = 0
        t = 0
        p = 0
        for name, value in zip(test_point_name_list, value_list):
            if "温度" in name:
                t = (value + t_n * t) / (t_n + 1)
                t_n = t_n + 1
            elif "压力" in name:
                p = (value + p_n * p) / (p_n + 1)
                p_n = p_n + 1
            elif "流量" in name:
                self.mass_flow = value
        if t != 0:
            self.t = t
        if p != 0:
            self.p = p
        if self.p != -1 and self.t != -1:
            self.available = True
            self.h = get_h_by_pt(p, t + 273.15)


class Case:
    """
    定义单个试验工况的数据组合，用于完成热耗、缸效率等的计算
    """
    parameters_available = {}  # 可用参数字典
    time_period = {}  # 性能试验数据采集时间段
    main_steam: "主蒸汽,主汽门前" = TestPoint()  # 不区分是左侧还是右侧主汽门
    adjust_steam: "调节级" = TestPoint()
    outlet_high: "高压缸排汽" = TestPoint()
    inlet_medium: "再热汽门前,热再,再热蒸汽" = TestPoint()
    outlet_medium: "中排,中压缸排汽" = TestPoint()
    inlet_low: "低压缸进汽" = TestPoint()
    outlet_low: "低压缸排汽" = TestPoint()
    extract_1: "一段抽汽" = TestPoint()
    heater_1_vapor_in: "一号高加进汽" = TestPoint()
    heater_1_vapor_out: "一号高加疏水" = TestPoint()
    heater_1_water_in: "一号高加进水" = TestPoint()
    heater_1_water_out: "一号高加出水" = TestPoint()
    extract_2: "二段抽汽" = TestPoint()
    heater_2_vapor_in: "二号高加进汽" = TestPoint()
    heater_2_vapor_out: "二号高加疏水" = TestPoint()
    heater_2_water_in: "二号高加进水" = TestPoint()
    heater_2_water_out: "二号高加出水" = TestPoint()
    extract_3: "三段抽汽" = TestPoint()
    heater_pre_3: "三号高加外置蒸冷器进汽,三抽蒸冷器" = TestPoint()
    heater_3_vapor_in: "三号高加进汽" = TestPoint()
    heater_3_vapor_out: "三号高加疏水" = TestPoint()
    heater_3_water_in: "三号高加进水" = TestPoint()
    heater_3_water_out: "三号高加出水" = TestPoint()
    extract_4: "四段抽汽" = TestPoint()
    heater_4_vapor_in: "四号高加进汽" = TestPoint()
    heater_4_vapor_out: "四号高加疏水" = TestPoint()
    heater_4_water_in: "四号高加进水" = TestPoint()
    heater_4_water_out: "四号高加出水" = TestPoint()
    extract_5: "五段抽汽" = TestPoint()
    heater_5_vapor_in: "五号低加进汽" = TestPoint()
    heater_5_vapor_out: "五号低加疏水" = TestPoint()
    heater_5_water_in: "五号低加进水" = TestPoint()
    heater_5_water_out: "五号低加出水" = TestPoint()
    extract_6: "六段抽汽" = TestPoint()
    heater_6_vapor_in: "六号低加进汽" = TestPoint()
    heater_6_vapor_out: "六号低加疏水" = TestPoint()
    heater_6_water_in: "六号低加进水" = TestPoint()
    heater_6_water_out: "六号低加出水" = TestPoint()
    extract_7: "七段抽汽" = TestPoint()
    heater_7_vapor_in: "七号低加进汽" = TestPoint()
    heater_7_vapor_out: "七号低加疏水" = TestPoint()
    heater_7_water_in: "七号低加进水" = TestPoint()
    heater_7_water_out: "七号低加出水" = TestPoint()
    extract_8: "八段抽汽" = TestPoint()
    heater_8_vapor_in: "八号低加进汽" = TestPoint()
    heater_8_vapor_out: "八号低加疏水" = TestPoint()
    heater_8_water_in: "八号低加进水" = TestPoint()
    heater_8_water_out: "八号低加出水" = TestPoint()
    seal_heater_1: "一号轴加进水,轴加进水" = TestPoint()
    seal_heater_2: "二号轴加进水,-轴加进水" = TestPoint()  # 包含二号轴加进水，排除轴加进水

    deaerator_vapor_inlet: "除氧器进汽" = TestPoint()
    pump_turbine_inlet: "小机进汽,给水泵汽轮机进汽" = TestPoint()

    heat_well_outlet: "热井出" = TestPoint()
    water_condense_pump_outlet: "凝泵出,凝结水泵出" = TestPoint()
    main_condense_water: "主凝结水" = TestPoint()
    deaerator_water_inlet: "除氧器进水" = TestPoint()
    deaerator_outlet: "除氧器出水,除氧器下水" = TestPoint()
    feed_pump_outlet: "给水泵出" = TestPoint()
    final_feed_water: "最终给水" = TestPoint()
    water_reheater_reducing: "再热减温水,再减,再热器减温水" = TestPoint()
    water_overheat_reducing_1: "过热一级减温水" = TestPoint()
    water_overheat_reducing_2: "过热二级减温水" = TestPoint()
    p_env: "大气压力" = 0
    condense_water_level: "凝汽器水位" = 0
    deaerator_water_level: "除氧器水位" = 0

    leakage_hp_to_extract_3: "高压门杆漏气至三抽" = TestPoint()

    def set_value_of_test_point(self, var_str, test_point_name_list, value_list):
        """
        根据计算程序参数对应的 所有测点的名称和值 给计算程序中测点水/水蒸气赋状态

        :param var_str:
        :param test_point_name_list:
        :param value_list:
        :return:
        """
        obj = getattr(self, var_str)
        if isinstance(obj, TestPoint):
            obj.set_state_by_name_and_value_list(test_point_name_list, value_list)
        else:
            setattr(self, var_str, float(value_list))


# power_station_annotations = sys.modules[__name__].__annotations__
alternative_symbol = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七",
                      "8": "八", "9": "九", "汽": "气", "0": "零", "零": "〇", "进": "入", "一轴加": "一号轴加", "A": "a",
                      "B": "b"}

# 数据采集系统中为绝对压力的测点
pressure_absolute = ["低排", "低压缸排汽", "小机排汽", "七段抽汽", "八段抽汽", "高压汽源至汽封蒸汽冷却器进汽压力",
                     "大气压", "环境压力", "七号低加", "7号低加", "8A低加", "8B低加", "9A低加", "9B低加",
                     # "高压缸前后轴封", "中压缸前轴封", "中压缸后轴封","轴封加热器进汽压力", "高压缸前后轴封漏汽母管",
                     ]

# 数据采集系统中为相对压力的测点
pressure_relative = ["主汽门", "调节级", "高压缸排汽", "再热蒸汽", "再热汽门", "中压缸进汽", "中压缸排汽",
                     "低压缸进汽", "一段抽汽", "二段抽汽",
                     "三段抽汽", "四段抽汽", "五段抽汽", "六段抽汽", "高加进汽", "高加", "5号低加", "6号低加", "小机进汽",
                     "除氧器进汽",
                     "最终给水", "给水泵出水", "凝泵", "再热减温水", "高压门杆漏汽",
                     "蒸汽冷却器",
                     "低温省煤器进水压力", "低温省煤器",
                     "蒸冷器", "低省", "凝结水", "前置泵", "汽泵", "循环水"]
