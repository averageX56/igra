file = open('chuncks.txt','w')
house1 = [44, 45, 69, 70]
house2 = [47, 48, 72, 73]
house3 = [403, 404, 428, 429]
house4 = [406, 407, 431, 432]
house5 = [409, 410, 434, 435]
house6 = [413, 414, 438, 439]
house7 = [416, 417, 441, 442]
house8 = [419, 420, 444, 445]
house9 = [422, 423, 447, 448]
house10 = [460, 461, 485, 486]
house11 = [477, 478, 502, 503]
house12 = [482, 483, 507, 508]
house13 = [489, 490, 514, 515]
house14 = [496, 497, 521, 522]
house15 = [551, 552, 576, 577]
house16 = [554, 555, 579, 580]
house17 = [557, 558, 582, 583]
house18 = [563, 564, 588, 589]
house19 = [566, 567, 591, 592]
house20 = [570, 571, 595, 596]
study_bilding1 = [32, 33, 34, 57, 58, 59, 82, 83, 84]
study_bilding2 = [40,41,42, 65, 66, 67, 90, 91, 92]
study_bilding3 = [53,54,55, 78, 79, 80, 103, 104, 105]
study_bilding4 = [86,87,88, 111, 112, 113, 136, 137, 138]
study_bilding5 = [119, 120, 121, 144, 145, 146, 169, 170, 171]
study_bilding6 = [155, 156, 157, 180, 181, 182, 205, 206, 207]
small_building1 = [220, 221, 245, 246]
small_building2 = [217, 218, 242, 243]
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
    elif i in small_building1:
        file.write(str(i) + '  sml1' + '\n')
    elif i in small_building2:
        file.write(str(i) + '  sml2' + '\n')
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
    elif i in house19:
        file.write(str(i) + '  hs19' + '\n')
    elif i in house20:
        file.write(str(i) + '  hs20' + '\n')
    else:
        file.write(str(i) + '  map' + '\n')

file.close()
