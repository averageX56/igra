
food1 = [44, 45, 69, 70]
food2 = [47, 48, 72, 73]
house1 = [403, 404, 428, 429]
house2 = [406, 407, 431, 432]
house3 = [409, 410, 434, 435]
house10 = [413, 414, 438, 439]
house11 = [416, 417, 441, 442]
house12 = [419, 420, 444, 445]
house13 = [422, 423, 447, 448]
house4 = [460, 461, 485, 486]
house5 = [477, 478, 502, 503]
house6 = [482, 483, 507, 508]
house14 = [489, 490, 514, 515]
house15 = [496, 497, 521, 522]
house7 = [551, 552, 576, 577]
house8 = [554, 555, 579, 580]
house9 = [557, 558, 582, 583]
house16 = [563, 564, 588, 589]
house17 = [566, 567, 591, 592]
house18 = [570, 571, 595, 596]
study_bilding1 = [32, 33, 34, 57, 58, 59, 82, 83, 84]
study_bilding2 = [40,41,42, 65, 66, 67, 90, 91, 92]
study_bilding3 = [53,54,55, 78, 79, 80, 103, 104, 105]
study_bilding4 = [86,87,88, 111, 112, 113, 136, 137, 138]
study_bilding5 = [119, 120, 121, 144, 145, 146, 169, 170, 171]
study_bilding6 = [155, 156, 157, 180, 181, 182, 205, 206, 207]
shop1 = [220, 221, 245, 246]
shop2 = [217, 218, 242, 243]
buldings = [food1, food2, house1, house2, house3, house4, house5, house6, house7, house8, house9, house10,house11, house12, house13, house14, house15, house16, house17, house18,
            study_bilding1, study_bilding2, study_bilding3, study_bilding4, study_bilding5, study_bilding6, shop1, shop2]
building_textures_std = [['GK1','GK2','GK3','GK4','GK5','GK6','GK7','GK8','GK9'], ['LK1', 'LK2','LK3','LK4','LK5','LK6','LK7','LK8','LK9'],
                         ['CIFRA1','CIFRA2','CIFRA3','CIFRA4','CIFRA5','CIFRA6','CIFRA7','CIFRA8','CIFRA9'],
                         ['NK1','NK2','NK3','NK4','NK5','NK6','NK7','NK8','NK9'],
                         ['ARKTICA1','ARKTICA2','ARKTICA3','ARKTICA4','ARKTICA5','ARKTICA6','ARKTICA7','ARKTICA8','ARKTICA9'],
                         ['KPM1','KPM2','KPM3','KPM4','KPM5','KPM6','KPM7','KPM8','KPM9']]
building_textures_hs_right = [['dm'+str(i)+'_'+str(j) for j in range(1,5)] for i in range(1,5)]
building_textures_hs_right.append(['sport11','sport12','sport13','sport14'])
building_textures_hs_right += [['dm'+str(i)+'_'+str(j) for j in range(1,5)] for i in range(5,8)]
building_textures_hs_right.append(['sport01','sport02','sport03','sport04'])
building_textures_hs_left = [['dm'+str(i)+'_'+str(j) for j in range(1,5)] for i in range(8,12)]
building_textures_hs_left.append(['sport21','sport22','sport23','sport24'])
building_textures_hs_left += [['dm'+str(i)+'_'+str(j) for j in range(1,5)] for i in range(12,15)]
building_textures_hs_left.append(['food11','food12','food13','food14'])
building_textures_food = [[x + str(j) for j in range(1, 5)] for x in ['KSP', 'shop', 'food3', 'food2']]
open_chuncks = ['std1','std2','std3','std4','std5','std6','shop1','shop2','food1','food2','hs1','hs2','hs3','hs4','hs5','hs6','hs7','hs8','hs9','hs10','hs11','hs12','hs13','hs14','hs15','hs16','hs17','hs18']

def obnul():
    file = open('chuncks.txt', 'w')
    for i in range(625):
        if i in study_bilding1:
            file.write(str(i)+'  std1'+'\n')
        elif i in study_bilding2:
            file.write(str(i) + '  std2' + '\n')
        elif i in study_bilding3:
            file.write(str(i) + '  std3' + '\n')
        elif i in study_bilding4:
            file.write(str(i) + '  std4' + '\n')
        elif i in study_bilding5:
            file.write(str(i) + '  std5' + '\n')
        elif i in study_bilding6:
            file.write(str(i) + '  std6' + '\n')
        elif i in shop1:
            file.write(str(i) + '  shop1' + '\n')
        elif i in shop2:
            file.write(str(i) + '  shop2' + '\n')
        elif i in house1:
            file.write(str(i) + '  hs1' + '\n')
        elif i in house2:
            file.write(str(i) + '  hs2' + '\n')
        elif i in house3:
            file.write(str(i) + '  hs3' + '\n')
        elif i in house4:
            file.write(str(i) + '  hs4' + '\n')
        elif i in house5:
            file.write(str(i) + '  hs5' + '\n')
        elif i in house6:
            file.write(str(i) + '  hs6' + '\n')
        elif i in house7:
            file.write(str(i) + '  hs7' + '\n')
        elif i in house8:
            file.write(str(i) + '  hs8' + '\n')
        elif i in house9:
            file.write(str(i) + '  hs9' + '\n')
        elif i in house10:
            file.write(str(i) + '  hs10' + '\n')
        elif i in house11:
            file.write(str(i) + '  hs11' + '\n')
        elif i in house12:
            file.write(str(i) + '  hs12' + '\n')
        elif i in house13:
            file.write(str(i) + '  hs13' + '\n')
        elif i in house14:
            file.write(str(i) + '  hs14' + '\n')
        elif i in house15:
            file.write(str(i) + '  hs15' + '\n')
        elif i in house16:
            file.write(str(i) + '  hs16' + '\n')
        elif i in house17:
            file.write(str(i) + '  hs17' + '\n')
        elif i in house18:
            file.write(str(i) + '  hs18' + '\n')
        elif i in food1:
            file.write(str(i) + '  food1' + '\n')
        elif i in food2:
            file.write(str(i) + '  food2' + '\n')
        else:
            file.write(str(i) + '  map' + '\n')
    file.close()
cost = [[1500, 1300, 1800, 0, 0, 1500, 1300, 1800, 0, 0], [400, 300, 350, 400, 750, 500, 666, 400, 700, 700], [400, 300, 350, 400, 750, 500, 666, 400, 700, 700], [700, 600, 0, 0, 0, 500, 500, 500, 500, 500]]
#obnul()
