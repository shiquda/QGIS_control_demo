from qgis.core import QgsProject
import time
import csv

def change_color(id, colour):
    '''
    :param id: 红绿灯的id
    :param colour: 红绿灯的颜色，0为绿色，1为红色，2为黄色，3为左转绿色
    '''
    layer = QgsProject.instance().mapLayersByName("红绿灯")[0]
    for i in range(layer.featureCount()):
        feature = layer.getFeature(i)
        current_id = feature['id']
        if current_id == id:
            feature['colour'] = colour
            layer.updateFeature(feature)
            # print('修改成功')
            break
# # 定义颜色字典
# colour_dict = {0: 'green', 1: 'red', 2: 'yellow'}

light_map = {
    '红绿灯1': [10, 11, 12, 13],
    '红绿灯2': [17, 18],
    '红绿灯3': [14, 15, 16],
    '红绿灯4': [19],
    '红绿灯5': [8, 9],
    '红绿灯6': [1, 2],
    '红绿灯7': [0, 3],
    '红绿灯8': [4, 5],
    '红绿灯9': [6, 7],
}

with open('E:\\repo\\!Others\\QGIS\\traffic_lights.csv', 'r', encoding='utf-8-sig') as f:
    # 读取文件内容,第一列是时间信息(秒),后面9列是红绿灯的颜色信息
    reader = csv.reader(f)
    # 读取列
    is_first_row = True
    for row in reader:
        if is_first_row:
            is_first_row = False
            continue
        print(row)
        # 读取每一行
        delay_time = int(row[0])
        for i in range(1,10):
            # 读取每一列
            light_id = light_map[f'红绿灯{i}']
            light_colour = int(row[i])
            print(light_id, light_colour)
            for j in light_id:
                change_color(j, light_colour)
        time.sleep(delay_time / 50)
