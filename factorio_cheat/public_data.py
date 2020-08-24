"""
    :param path: 要修改的文件的地址
    :param specified_front_num: front_str出现的次数（出现指定次数后才是真正的定位符）
    :param specified_target_num: target_str出现的次数。自行指定，一般设定为1，即目标字符串第一次出现就确定。
    :param front_str: 要修改字符串的前导字符（用于定位要修改的字符串）
    :param target_str: 定位符（后面就是要修改的字符串）
    :param new_cheat_str: 修改后的字符串
    specified_front_num和front_str是相关的，要同时修改
"""
CHEAT_DICT = {
    'player_hp': {
        # 修改玩家生命
        # name = "character",
        # 修改玩家生命80000
        'cn_name': '玩家生命',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "character"',
        'target_str': 'max_health = ',
        'new_cheat_str': 95000,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'hp_resume': {
        # 每秒生命回复200
        'cn_name': '每秒生命回复',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "character"',
        'target_str': 'healing_per_tick = ',
        'new_cheat_str': 200,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'pack_space': {
        # 背包容量130
        'cn_name': '背包容量',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "character"',
        'target_str': 'inventory_size = ',
        'new_cheat_str': 130,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'running_speed': {
        # 跑步速度0.4
        'cn_name': '跑步速度',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "character"',
        'target_str': 'running_speed = ',
        'new_cheat_str': 0.4,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'wire_pole_hp': {
        # name = "small-electric-pole"
        # 小电线杆HP35000
        'cn_name': '小电线杆HP',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "small-electric-pole"',
        'target_str': 'max_health = ',
        'new_cheat_str': 35000,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'wire_pole_interval': {
        # 连接距离40
        'cn_name': '小电线杆连接距离',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "small-electric-pole"',
        'target_str': 'maximum_wire_distance = ',
        'new_cheat_str': 40,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'wire_pole_cover_area': {
        # 覆盖面积9
        'cn_name': '小电线杆覆盖面积',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "small-electric-pole"',
        'target_str': 'supply_area_distance = ',
        'new_cheat_str': 9,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'pipe_hp': {
        # 修改地下管道HP
        # name = "pipe-to-ground"
        # 地下管道HP35000
        'cn_name': '地下管道HP',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "pipe-to-ground"',
        'target_str': 'max_health = ',
        'new_cheat_str': 35000,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'pipe_length': {
        # 长度250
        'cn_name': '地下管道长度',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "pipe-to-ground"',
        'target_str': 'max_underground_distance = ',
        'new_cheat_str': 250,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'wall_hp': {
        # 石墙修改95000
        # name = "stone-wall"
        'cn_name': '石墙HP',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "stone-wall"',
        'target_str': 'max_health = ',
        'new_cheat_str': 95000,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'lab_efficiency': {
        # 研究中心研发速度
        # name = "lab"
        'cn_name': 'lab研发速度',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "lab"',
        'target_str': 'researching_speed = ',
        'new_cheat_str': 10,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'lab_slots': {
        # 研究中心插槽
        # name = "lab"
        'cn_name': 'lab插槽',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "lab"',
        'target_str': 'module_slots = ',
        'new_cheat_str': 4,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'accumulator_capacity': {
        # 蓄电池容量
        # name = "accumulator"
        'cn_name': '蓄电池容量',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "accumulator"',
        'target_str': 'buffer_capacity = ',
        'new_cheat_str': 50,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'solar_panel_production': {
        # 太阳能板发电量
        # name = "solar-panel"
        'cn_name': '太阳能板发电量',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "solar-panel"',
        'target_str': 'production = ',
        'new_cheat_str': 600,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'beacon_area': {
        # name = "beacon"
        # 此项修改极端耗能，除非准备大量电源，否则不要放置此插件分享塔。
        # 范围修改20
        'cn_name': '插件分享塔范围',
        'path': r"entity\entities.lua",
        'front_str': 'name = "beacon"',
        'target_str': 'supply_area_distance = ',
        'new_cheat_str': 20,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'beacon_efficiency': {
        # 分享塔效率10
        'cn_name': '插件分享塔效率',
        'path': r"entity\entities.lua",
        'front_str': 'name = "beacon"',
        'target_str': 'distribution_effectivity = ',
        'new_cheat_str': 10,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'beacon_slots': {
        # 插孔4
        'cn_name': '插件分享塔插孔个数',
        'path': r"entity\entities.lua",
        'front_str': 'name = "beacon"',
        'target_str': 'module_slots = ',
        'new_cheat_str': 6,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'oil_min': {
        # 巨量石油修改
        # type = "resource"
        'cn_name': '石油最小值',
        'path': r"entity\resources.lua",
        'front_str': 'type = "resource"',
        'target_str': 'minimum = ',
        'new_cheat_str': 75,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'oil_normal': {
        'cn_name': '石油正常值',
        'path': r"entity\resources.lua",
        'front_str': 'type = "resource"',
        'target_str': 'normal = ',
        'new_cheat_str': 75,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'laser_turret_hp': {
        # type = "electric-turret"
        # 激光炮塔生命60000
        'cn_name': '激光炮塔生命',
        'path': r"entity\demo-turrets.lua",
        'front_str': 'type = "electric-turret"',
        'target_str': 'max_health = ',
        'new_cheat_str': 60000,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'laser_turret_cooldown': {
        # 冷却时间1
        'cn_name': '激光炮塔冷却时间',
        'path': r"entity\demo-turrets.lua",
        'front_str': 'type = "electric-turret"',
        'target_str': 'cooldown = ',
        'new_cheat_str': 1,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'laser_turret_range': {
        # 范围40
        'cn_name': '激光炮塔范围',
        'path': r"entity\demo-turrets.lua",
        'front_str': 'type = "electric-turret"',
        'target_str': 'range = ',
        'new_cheat_str': 40,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'laser_turret_damage_modifier': {
        # 机枪炮塔伤害系数20
        'cn_name': '机枪炮塔伤害系数',
        'path': r"entity\demo-turrets.lua",
        'front_str': 'type = "electric-turret"',
        'target_str': 'damage_modifier = ',
        'new_cheat_str': 20,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'gun_turret_hp': {
        # 修改机枪炮塔生命60000
        # name = "gun-turret"
        'cn_name': '机枪炮塔生命',
        'path': r"entity\demo-turrets.lua",
        'front_str': 'name = "gun-turret"',
        'target_str': 'max_health = ',
        'new_cheat_str': 60000,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'basic_bullet_damage': {
        # 修改基本弹伤害
        # name = "firearm-magazine"
        # damage = { amount = 800 , type = "physical"}
        'cn_name': '基本弹伤害',
        'path': r"item\demo-ammo.lua",
        'front_str': 'name = "firearm-magazine"',
        'target_str': 'damage = { amount = ',
        'new_cheat_str': 800,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'belt_distance': {
        # 地下普速传送带传输距离修改250
        # name = "underground-belt"
        'cn_name': '地下普速传送带传输距离',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "underground-belt"',
        'target_str': 'max_distance = ',
        'new_cheat_str': 250,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'fast_belt_distance': {
        # 地下高速传送带传输距离修改250
        # name = "fast-underground-belt"
        'cn_name': '地下高速传送带传输距离',
        'path': r"entity\demo-entities.lua",
        'front_str': 'name = "fast-underground-belt"',
        'target_str': 'max_distance = ',
        'new_cheat_str': 250,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    'express_belt_distance': {
        # 地下急速传送带传输距离修改250
        # name = "express-underground-belt"
        'cn_name': '地下急速传送带传输距离',
        'path': r"entity\entities.lua",
        'front_str': 'name = "express-underground-belt"',
        'target_str': 'max_distance = ',
        'new_cheat_str': 250,
        'specified_front_num': 1,
        'specified_target_num': 1
    },
    "electric-mining-drill-speed": {
        # 电采矿机采矿速度
        # name = "electric-mining-drill"
        'cn_name': '电采矿机采矿速度',
        'path': r"entity\demo-mining-drill.lua",
        'front_str': 'name = "electric-mining-drill"',
        'target_str': 'mining_speed = ',
        'new_cheat_str': 5,
        'specified_front_num': 1,
        'specified_target_num': 1
    }
}

README = """
    Copyright@2020 liqiochi. All Rights Reserved.\n
    --------------------------------------------------------------------
    使用说明：先“打开安装目录”，在点“初始化修改数据”，第一次运行前最好点击“备份”。
    之后若要恢复，只需要点击“还原”即可。
    --------------------------------------------------------------------
    适用于Factorio v1.00。
    修改玩家生命95000，每秒生命回复200，背包容量130，跑步速度0.4。
    修改小电线杆HP35000，连接距离40，覆盖面积9。
    修改地下管道HP35000，长度250。
    修改基本弹伤害800。
    修改炮塔生命60000。
    修改石墙生命95000。
    修改地下普速/高速/急速传送带传输距离250（不要超过256）。
    修改插件分享塔覆盖面积20，插件效率10，插槽个数6。
    修改几乎无限石油（关于石油数值的两项修改最好不要改，除非你知道更好的值）。
    激光炮塔冷却时间降为1，伤害系数为40。
    修改电采矿机采矿速度为5
    --------------------------------------------------------------------
    注意！！！
    别改太多，否则索然无味！！！
    """

    # TODO: 太阳能板和蓄电池
"""
demo-entities.lua
name = "solar-panel"
max_health = 200
production = "60kW"


name = "accumulator"
max_health = 150,
buffer_capacity = "5MJ",
input_flow_limit = "300kW",
output_flow_limit = "300kW"
charge_cooldown = 30,
discharge_cooldown = 60,
"""