import numpy as np
import xlrd
import math
import xlwt
import tkinter.messagebox
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import os
def f(pr0,pr1,pr2,pr3,savepath,time_pre_treatment,t65):
    global e3,e4
    pr0 = xlrd.open_workbook(pr0)
    pr1 = xlrd.open_workbook(pr1)
    pr2 = xlrd.open_workbook(pr2)
    pr3 = xlrd.open_workbook(pr3)

    #预处理时间
    #计算
    #time_calculation = 5
    # 总运行时间
    #titime = time_pre_treatment + time_calculation



    tfinal_body = xlwt.Workbook()
    sheet11 = tfinal_body.add_sheet('tfinal_body')
    sheet11.write(0, 0, 'TIME')
    sheet11.write(0, 1, 'Tmsk')
    sheet11.write(0, 2, 'T_skin_head')
    sheet11.write(0, 3, 'T_skin_chest')
    sheet11.write(0, 4, 'T_skin_back')
    sheet11.write(0, 5, 'T_skin_abdomen')
    sheet11.write(0, 6, 'T_skin_L_uarm')
    sheet11.write(0, 7, 'T_skin_R_uarm')
    sheet11.write(0, 8, 'T_skin_L_larm')
    sheet11.write(0, 9, 'T_skin_R_larm')
    sheet11.write(0, 10, 'T_skin_L_hand')
    sheet11.write(0, 11, 'T_skin_R_hand')
    sheet11.write(0, 12, 'T_skin_L_thigh')
    sheet11.write(0, 13, 'T_skin_R_thigh')
    sheet11.write(0, 14, 'T_skin_L_calf')
    sheet11.write(0, 15, 'T_skin_R_calf')
    sheet11.write(0, 16, 'T_skin_L_foot')
    sheet11.write(0, 17, 'T_skin_R_foot')
    sheet11.write(0, 18, 'T_core_abdomen')

    for cid in range(1,8): #从1到7循环
        # 创建表格写入数据
        T_body = xlwt.Workbook()
        TSV = xlwt.Workbook()
        TCV = xlwt.Workbook()
        # 写入表头
        # 皮肤温度及腹部核心温度
        sheet1 = T_body.add_sheet('T_body')
        sheet1.write(0, 0, 'TIME')
        sheet1.write(0, 1, 'Tmsk')
        sheet1.write(0, 2, 'T_skin_head')
        sheet1.write(0, 3, 'T_skin_chest')
        sheet1.write(0, 4, 'T_skin_back')
        sheet1.write(0, 5, 'T_skin_abdomen')
        sheet1.write(0, 6, 'T_skin_L_uarm')
        sheet1.write(0, 7, 'T_skin_R_uarm')
        sheet1.write(0, 8, 'T_skin_L_larm')
        sheet1.write(0, 9, 'T_skin_R_larm')
        sheet1.write(0, 10, 'T_skin_L_hand')
        sheet1.write(0, 11, 'T_skin_R_hand')
        sheet1.write(0, 12, 'T_skin_L_thigh')
        sheet1.write(0, 13, 'T_skin_R_thigh')
        sheet1.write(0, 14, 'T_skin_L_calf')
        sheet1.write(0, 15, 'T_skin_R_calf')
        sheet1.write(0, 16, 'T_skin_L_foot')
        sheet1.write(0, 17, 'T_skin_R_foot')
        sheet1.write(0, 18, 'T_core_abdomen')

        # 热感觉
        sheet2 = TSV.add_sheet('TSV')
        sheet2.write(0, 0, 'TIME')
        sheet2.write(0, 1, 'So') # 整体热感觉
        sheet2.write(0, 2, 'head')
        sheet2.write(0, 3, 'chest')
        sheet2.write(0, 4, 'back')
        sheet2.write(0, 5, 'abdomen')
        sheet2.write(0, 6, 'L_uarm')
        sheet2.write(0, 7, 'R_uarm')
        sheet2.write(0, 8, 'L_larm')
        sheet2.write(0, 9, 'R_larm')
        sheet2.write(0, 10, 'L_hand')
        sheet2.write(0, 11, 'R_hand')
        sheet2.write(0, 12, 'L_thigh')
        sheet2.write(0, 13, 'R_thigh')
        sheet2.write(0, 14, 'L_calf')
        sheet2.write(0, 15, 'R_calf')
        sheet2.write(0, 16, 'L_foot')
        sheet2.write(0, 17, 'R_foot')

        # 热舒适
        sheet3 = TCV.add_sheet('TCV')
        sheet3.write(0, 0, 'TIME')
        sheet3.write(0, 1, 'tcvo') # 整体热感觉
        sheet3.write(0, 2, 'head')
        sheet3.write(0, 3, 'chest')
        sheet3.write(0, 4, 'back')
        sheet3.write(0, 5, 'abdomen')
        sheet3.write(0, 6, 'L_uarm')
        sheet3.write(0, 7, 'R_uarm')
        sheet3.write(0, 8, 'L_larm')
        sheet3.write(0, 9, 'R_larm')
        sheet3.write(0, 10, 'L_hand')
        sheet3.write(0, 11, 'R_hand')
        sheet3.write(0, 12, 'L_thigh')
        sheet3.write(0, 13, 'R_thigh')
        sheet3.write(0, 14, 'L_calf')
        sheet3.write(0, 15, 'R_calf')
        sheet3.write(0, 16, 'L_foot')
        sheet3.write(0, 17, 'R_foot')




        ## 1.基本参数定义 ##
        # 以下矩阵若无特别说明，则各列分别代表[头、胸、背、腹、左大臂、右大臂、左小臂、右小臂、左手、右手、左大腿、右大腿、左小腿、右小腿、左足、右足]，共十六个节段。
        # (1)各节段皮肤表面积ADu(单位m^2)与重量weight(单位kg)
        adu = pr1.sheets()[0]
        sa = 1.87
        weight = pr1.sheets()[1]  # 所有参数单独一个sheet表

        # （2）各节点比热容C（单位Wh/℃），各行分别代表[核心、肌肉、脂肪、皮肤]
        c = pr1.sheets()[2]#读入第三个sheet表
        c65 = 2.610
        c_head_core = c.cell(1, 1).value#读入[2,2]单元格

        # （3）各节点之间热导率Cd（单位W/℃）,各行分别代表[核心-肌肉、肌肉-脂肪、脂肪-皮肤]
        cd = pr1.sheets()[3]  # tc-Ymodel

        # （4）各节点基本代谢率Qb (单位W),各行分别代表[核心、肌肉、脂肪、皮肤]
        qb = pr1.sheets()[4]

        # （5）各节点基本血流量BFB(单位l/h),各行分别代表[核心、肌肉、脂肪、皮肤]
        bfb = pr1.sheets()[5]
        bfb65 = 282.016
        bfb_head_core = bfb.cell(1, 1).value

        # （6）各节点冷热误差信号计算基准值Tset(单位℃),各行分别代表[核心、肌肉、脂肪、皮肤]
        tset = pr1.sheets()[6]
        tskin_set = tset.row_values(4)

        t = np.zeros(shape=(5, 16))
        for i in range(1, 17):
            for j in range(1, 6):
                t[j - 1, i - 1] = tset.cell(j, i).value

        tset_blood = 36.7

        # （7）权重/分配系数（包括做功分配系数Metf，误差信号求和权重系数SKINR、皮肤层出汗分配系数SKINS、
        # 皮肤层血管舒张分配系数SKINV、皮肤层血管收缩分配系数SKINC、肌肉层寒颤产热分配系数Chilf）
        metf = pr1.sheets()[7]  # workm-Ymodel
        skinr = pr1.sheets()[8]
        skins = pr1.sheets()[9]
        skinv = pr1.sheets()[10]
        skinc = pr1.sheets()[11]
        chilf = pr1.sheets()[12]

        # （8）主动系统控制系数（出汗Csw、Ssw、Psw，寒颤Cch、Sch、Pch，血管收缩/舒张Cdl、Sdl、Pdl、Cst、Sst、Pst）
        csw = 371.2
        ssw = 33.6
        psw = 0
        cch = 0
        sch = 0
        pch = 24.4
        cdl = 117  # 舒张c
        sdl = 7.5
        pdl = 0
        cst = 11.5  # 收缩c
        sst = 11.5
        pst = 0

        # （9）刘易斯系数LR（对于典型的室内环境，LR=16.5 ℃/kPa）、各节段服装显热热阻clo(单位clo)、衣物水蒸气渗透效率icl与服装面积系数fcl（Icl、icl与fcl取值可参考《建筑环境学（第三版）》附录4-1，用于算蒸发换热系数he等参数）
        lr = 16.5
        clo = pr2.sheets()[0]
        icl = pr2.sheets()[1]
        fcl = np.zeros((1, 16))
        for i in range(1, 17):
            fcl[0, i - 1] = 1.00 + 0.25 * clo.cell(1, i).value

        aaa = fcl[0, 0]
        # （10）各节段对流换热系数hc、辐射换热系数hr(单位(kcal/h)/(m^2·K)，换热系数由暖体假人实验测试得到，若无实验条件，可参考相关文献)
        hc = pr2.sheets()[2]
        hr = pr2.sheets()[3]
        qr = pr2.sheets()[4]  # 辐射换热量

        # （11）各节段热感觉及热舒适模型相关参数
        c1 = pr3.sheets()[0]
        k1 = pr3.sheets()[1]
        c2 = pr3.sheets()[2]
        c3 = pr3.sheets()[3]
        c31 = pr3.sheets()[4]
        c32 = pr3.sheets()[5]
        c6 = pr3.sheets()[6]
        c71 = pr3.sheets()[7]
        c72 = pr3.sheets()[8]
        c8 = pr3.sheets()[9]
        n = pr3.sheets()[10]
        aa = pr3.sheets()[11]
        bb = pr3.sheets()[12]
        cc = pr3.sheets()[13]


        ## 2.参数初始化 ##
        # 各节点温度初始化
        tclo = np.zeros((1, 16))
        # 冷热误差信号
        err = np.zeros((4, 16))
        # km为将皮肤温度效应与血管收缩/舒张联系起来的中间参数
        km = np.zeros((1, 16))
        # 皮肤层各节点出汗散热量
        esw = np.zeros((1, 16))
        # 肌肉层各节点寒颤产热量
        ch = np.zeros((1, 16))
        # 皮肤层与环境传热——显热-裸体
        qskin_env_se = np.zeros((1, 16))
        # 皮肤表面可能达到的最大潜热换热量
        emax = np.zeros((1, 16))
        # 皮肤表面蒸发换热量
        esk = np.zeros((1, 16))
        # 皮肤层饱和水蒸气分压力
        pskin_sat = np.zeros((1, 16))
        # 血流量
        bf = np.zeros((4, 16))
        # 总产热量
        q_heatproduct = np.zeros((4, 16))
        # 血液传热量
        q_blood = np.zeros((4, 16))
        # 组织间传热量
        q_conduct = np.zeros((3, 16))
        # 组织层的热流
        hf = np.zeros((5, 16))
        # 组织层的单位时间变化率
        dt = np.zeros((5, 16))
        # q 某节点新陈代谢总产热量
        q = np.zeros((4, 16))
        # e 皮肤层蒸发散热总量
        e = np.zeros((5, 16))
        # 服装面对流质交换系数
        he = np.zeros((1, 16))
        # 皮肤表面水蒸气分压
        pskin = np.zeros((1, 16))
        # 无感蒸发散热量
        eb = np.zeros((1, 16))

        warm = np.zeros((4, 16))

        cold = np.zeros((4, 16))
        qcloi = np.zeros((5, 16))
        q_floor = np.zeros((5, 16))
        q_cv = np.zeros((5, 16))  # 对流传热
        q_r = np.zeros((5, 16))
        bc = np.zeros((4, 16))  # 血液传热 q_blood
        td = np.zeros((4, 16)) # 节点导热
        # 创建空的做功矩阵
        worki = np.zeros(shape=(1, 16))
        # worki=np.array(worki)
        met = 1.0
        # 人体基础代谢0.778met；静坐1.1met 多余的根据代谢水平计算各个节段肌肉做功
        for i in range(1, 17):
            if met > 0.778:
                worki[0, i - 1] = 58.2 * (met - 0.778) * sa * metf.cell(1, i).value  # 计算16个节段每一段做功分配

            else:
                worki[0, i - 1] = 0

        # 初始局部热感觉计算,目前由于t=tset,各节段tsv0计算值为 0
        tsv = np.zeros((1, 16))  #初始化局部热感觉
        tsv0 = np.zeros((1, 16)) #初始局部热感觉
        tmsk = 0
        tset_msk = 0
        for i in range(1, 17):
            tmsk = tmsk + t[3, i - 1] * c.cell(4, i).value / 3.894  # 3.894皮肤层各节点比热和；c/3.894得到各节段百分比
            tset_msk = tset_msk + tset.cell(4,i).value * c.cell(4, i).value / 3.894

        for i in range(1, 17):
            # 判断局部冷热，选择c1和k1的第x行的参数用于计算
            if (t[3, i-1] - tset.cell(4,i).value) < 0:
                x = 1
            else:
                x = 2
        tsv0[0,i-1] = 4 * (2/(1+np.exp(-c1.cell(x,i).value * (t[3,i-1]-tset.cell(4,i).value)-k1.cell(x,i).value*((t[3,i-1]-tmsk)-(tset.cell(4,i).value-tset_msk))))-1)

        # 初始化局部热舒适及中间参数
        tcv = np.zeros((1, 16))
        a = np.zeros((1, 16))
        right_slope = np.zeros((1, 16))
        offset = np.zeros((1, 16))
        maxcomfort = np.zeros((1, 16))

        ## 3.运行计算 ##
        evo = pr0.sheets()[0]#读入第1个sheet表
        caseid1 = evo.cell(1, 1).value# [2,2]单元格[行，列]



        time = 1
        time_dur=evo.cell(cid, 7).value
        # 总运行时间
        int_a = int(float(time_dur))

        titime = time_pre_treatment + int_a
        tout = np.zeros(shape=(titime + 1, 16))

        while time < titime: #预处理阶段
            if time < time_pre_treatment:
                Ta = 26  # 空气温度，℃
                Tg = 26  # 黑球温度，℃
                RH = 50  # 相对湿度，#
                V = 0.1  # 空气流速,m/s
            elif time < time_pre_treatment + time_dur: #读入稳态环境计算30分钟
                Ta = evo.cell(cid, 3).value  # 空气温度，℃
                Tg = evo.cell(cid, 4).value   # 黑球温度，℃
                RH = evo.cell(cid, 5).value   # 相对湿度，#
                V = evo.cell(cid, 6).value



            # 操作温度，℃
            Tr = ((Tg + 273)**4 + 2.5 * 10**8 * V**0.6 * (Tg-Ta))**0.25 - 273
            pair = 0.1 * np.exp(18.956 - 4030.183 / (Ta + 235)) * RH / 100
            tair = np.zeros((1,16))
            top = np.zeros((1, 16))

            for i in range(1, 17):
                tair[0,i-1] = Ta
                top[0,i-1] = (Ta+Tr)/2

            # ②冷热误差信号
            warms = 0  # 初始值清零
            colds = 0  # 初始值清零
            for i in range(1, 17):  # i节段
                for j in range(1, 5):
                    err[j - 1, i - 1] = t[j - 1, i - 1] - tset.cell(j, i).value
                    if err[j - 1, i - 1] < 0:
                        cold[j - 1, i - 1] = -err[j - 1, i - 1]
                        warm[j - 1, i - 1] = 0.0
                    else:
                        warm[j - 1, i - 1] = err[j - 1, i - 1]
                        cold[j - 1, i - 1] = 0.0
            for i in range(1, 17):
                warms = warms + warm[3, i - 1] * skinr.cell(1, i).value
                colds = colds + cold[3, i - 1] * skinr.cell(1, i).value

            # 计算出汗水平、dilat舒张水平、stric收缩水平、chill颤栗水平
            sweat = csw * err[0, 0] + ssw * (warms - colds) + psw * warm[0, 0] * warms
            if sweat < 0:
                sweat = 0
            dilat = cdl * err[0, 0] + sdl * (warms - colds) + pdl * warm[0, 0] * warms
            if dilat < 0:
                dilat = 0

            stric = -cst * err[0, 0] - sst * (warms - colds) + pst * cold[0, 0] * colds
            if stric < 0:
                stric = 0
            chill = -cch * err[0, 0] - sch * (warms - colds) + pch * cold[0, 0] * colds
            if chill < 0:
                chill = 0

            ##始计算不同节段不同层在这一时刻的代谢、肌肉层做功&颤栗、皮肤层的血管舒缩&出汗
            for i in range(1, 17):
                #产热量计算
                q[0, i - 1] = qb.cell(1, i).value
                q[1, i - 1] = qb.cell(2, i).value + worki[0, i - 1] + chilf.cell(1,i).value * chill  # i+1是因为有表头；肌肉层代谢需要考虑做功、颤栗  代谢=基础代谢+做功+颤栗
                q[2, i - 1] = qb.cell(3, i).value
                q[3, i - 1] = qb.cell(4, i).value

                # 血流量计算
                bf[0, i - 1] = bfb.cell(1, i).value  # 第i个节段 第一层基础血流量
                bf[1, i - 1] = bfb.cell(2, i).value + (q[1, i - 1] - qb.cell(2, i).value) / 1.16  # 肌肉层做功+寒颤会引起血流量变化 肌肉组织每产生1.16W的热量需要血流量1L/h;
                bf[2, i - 1] = bfb.cell(3, i).value
                bf[3, i - 1] = ((bfb.cell(4, i).value + skinv.cell(1, i).value * dilat)*(2**(err[3, i - 1]/10))/ (1 + skinc.cell(1, i).value * stric))

                #蒸发热量
                he[0, i - 1] = lr * icl.cell(1, i).value / (0.155 * clo.cell(1, i).value + icl.cell(1, i).value / (hc.cell(1, i).value * fcl[0, i - 1]))
                pskin[0, i - 1] = 0.1 * np.exp(18.956 - 4030.183 / (t[3, i - 1] + 235))  # 皮肤层饱和水蒸气压力，kpa
                emax[0, i - 1] = (pskin[0, i - 1] - pair) * he[0, i - 1] * adu.cell(1, i).value  # 该阶段皮肤温度表面达到的最大蒸发量
                esw[0, i - 1] = skins.cell(1, i).value * sweat * 2 ** (err[3, i - 1] / 10)  # 出汗汗液带走的热量，单位：W 出汗水平已经计算过
                eb[0, i - 1] = 0.06 * (1 - esw[0, i - 1] / emax[0, i - 1]) * emax[0, i - 1]  # 无感蒸发散热量 总是会有最大蒸发量的6%被蒸发
                if eb[0, i - 1] < 0:  # 基础蒸发量＜0时，取0
                    eb[0, i - 1] = 0
                e[0, i - 1] = 0
                e[1, i - 1] = 0
                e[2, i - 1] = 0  # 脂肪层无蒸发e=0
                e[3, i - 1] = eb[0, i - 1] + esw[0, i - 1]  # 已经考虑了有衣服无衣服的差别，第i个节段 皮肤层蒸发散热量
                if (e[3, i - 1] > emax[0, i - 1]):
                    e[3, i - 1] = emax[0, i - 1]  # 蒸发量限制在最大蒸发量值

            qz = 0
            for i in range(1, 17):
                for j in range(1, 5):
                    qz = qz + q[j - 1, i - 1]
            qz  # 各阶段各层的代谢总产热，呼吸散热量要用
            e[0, 1] = (0.0014 * (34 - tair[0, 0]) + 0.017 * (5.867 - pair)) * qz  # 呼吸散热单独计算，核心层-胸部：2节段

            ##计算总热量
            #血液传热
            for i in range(1, 17):
                for j in range(1, 5):
                    bc[j - 1, i - 1] = bf[j - 1, i - 1] * (t65 - t[j - 1, i - 1]) * 1.067

            #节点导热
            for i in range(1, 17):
                for j in range(1, 4):
                    td[j - 1, i - 1] = cd.cell(j, i).value * (t[j - 1, i - 1] - t[j, i - 1])  # 层与层之间导热
            #hf = np.zeros((5, 16))  # hf：传热功率Rate of heat flow into or from N 就是变化热量=热容c*温差T 开始计算热平衡方程
            # hf:单位W, 1Kcal/h(1千卡/时)=1.163W

            for i in range(1, 17):  # 1-8节段 上半身
                if (clo.cell(1, i).value == 0):  # 无衣服
                    q_cv[3, i - 1] = hc.cell(1, i).value * (4180/3600) * (t[3, i - 1] - tair[0,i - 1]) * adu.cell(1, i).value
                    # q_r[3,i-1]=qr.cell(1, i).value
                    q_r[3, i - 1] = hr.cell(1, i).value * (4180/3600) * (t[3, i - 1] - Tr)* adu.cell(1, i).value
                    hf[0, i - 1] = q[0, i - 1] + bc[0, i - 1] - td[0, i - 1] - e[0, i - 1]
                    hf[1, i - 1] = q[1, i - 1] + bc[1, i - 1] + td[0, i - 1] - td[1, i - 1]
                    hf[2, i - 1] = q[2, i - 1] + bc[2, i - 1] + td[1, i - 1] - td[2, i - 1]
                    hf[3, i - 1] = q[3, i - 1] + bc[3, i - 1] + td[2, i - 1] - e[3, i - 1] - q_cv[3, i - 1] - q_r[3, i - 1]

                else:  # 有衣服
                    qcloi[3, i - 1] = (t[3, i - 1] - t[4, i - 1]) / (0.155 * clo.cell(1, i).value) * adu.cell(1, i).value * fcl[0, i - 1]
                    e[4, i - 1] = e[3, i - 1]
                    q_cv[4, i - 1] = hc.cell(1, i).value * (4180/3600) * (t[4, i - 1] - tair[0,i - 1]) *  adu.cell(1, i).value * fcl[0, i - 1]
                    # q_r[4, i-1] = qr.cell(1, i).value
                    q_r[4, i - 1] = hr.cell(1, i).value * (4180/3600) * (t[3, i - 1] - Tr) * adu.cell(1, i).value* fcl[0, i - 1]
                    hf[0, i - 1] = q[0, i - 1] - e[0, i - 1] + bc[0, i - 1] - td[0, i - 1]
                    hf[1, i - 1] = q[1, i - 1] + bc[1, i - 1] + td[0, i - 1] - td[1, i - 1]
                    hf[2, i - 1] = q[2, i - 1] + bc[2, i - 1] + td[1, i - 1] - td[2, i - 1]
                    hf[3, i - 1] = q[3, i - 1] + bc[3, i - 1] + td[2, i - 1] - e[3, i - 1] - qcloi[3, i - 1]
                    hf[4, i - 1] = e[3, i - 1] + qcloi[3, i - 1] - e[4, i - 1] - q_cv[4, i - 1] - q_r[4, i - 1]
            # print(hf)
            ##

            # qcloi[5,14]
            hf65 = 0.0
            for i in range(1, 17):
                for j in range(1, 5):
                    hf65 = hf65 + bc[j - 1, i - 1]
            # 更新组织与血液温度
            #dt = np.zeros((5, 16))  ##dt 为每秒温度变化 比热c的单位是Wh/℃
            dttotal = 0
            for i in range(1, 17):
                for j in range(1, 5):
                    dt[j - 1, i - 1] = hf[j - 1, i - 1] / (c.cell(j, i).value * 3600)  # f 为每秒温度变化 比热c的单位是Wh/℃
                    t[j - 1, i - 1] = t[j - 1, i - 1] + dt[j - 1, i - 1]  # 更新各节点温度
                    dttotal = dttotal + dt[j - 1, i - 1]
                # 更新服装层
                dt[4, i - 1] = hf[4, i - 1] / (400 * 0.5)  # 服装比热取值为400J/(kg.℃)  *0.5为0.5kg衣服
                t[4, i - 1] = t[4, i - 1] + dt[4, i - 1]  # 更新服装
            # 更新血液
            dt65 = (-1) * hf65 / (c65 * 3600)  ###
            t65 = t65 + dt65
         # 计算平均皮肤温度 tmsk
            tmsk = 0
            for i in range(1, 17):
                tmsk = tmsk + t[3, i - 1] * c.cell(4, i).value / 3.894  # 3.894皮肤层各节点比热和；c/3.894得到各节段百分比
            tmsk
            # print(t)

            # 计算局部热感觉
            for i in range(1, 17):
                # 判断局部冷热，选择c1和k1的第x行的参数用于计算
                if (t[3, i-1] - tset.cell(4,i).value) < 0:
                    x = 1
                else:
                    x = 2
                # 判断局部皮肤温度升高/降低，选择c2第y行的参数用于计算
                if dt[3, i-1] < 0:
                    y = 1
                else:
                    y = 2

                tsv[0, i - 1] = 4 * (2 / (1 + np.exp(-c1.cell(x, i).value * (t[3, i-1] - tset.cell(4,i).value) - k1.cell(x, i).value * ((t[3, i-1] - tmsk) - (tset.cell(4,i).value - tset_msk)))) - 1) + c2.cell(y, i).value*dt[3,i-1] + c3.cell(1, i).value*dt[0,i-1]

                if tsv[0, i - 1] >= 4:
                    tsv[0, i - 1] = 4
                elif tsv[0, i - 1] <= -4:
                    tsv[0, i - 1] = -4


            #计算整体热感觉
            n_minus = 0
            n_plus = 0
            So = 0
            # 计算时手和脚各算一个部位，故此处剔除右手、右脚热感觉
            tsv14 = np.zeros((1, 14))
            tsv140 = np.zeros((1, 14))
            for i in range(1, 10):
                tsv14[0,i-1] = tsv[0,i-1]
                tsv140[0, i - 1] = tsv0[0, i - 1]
            for i in range(10, 15):
                tsv14[0, i - 1] = tsv[0, i]
                tsv140[0, i - 1] = tsv0[0, i]
            tsv_ascending = np.sort(tsv14,axis=1) # 对热感觉进行排序(升序)，axis = 1代表按行排序

            # 计算冷热感觉部位数量
            for i in range(1, 15):
                if tsv14[0,i-1] >= 0:
                    n_plus = n_plus + 1
                else:
                    n_minus = n_minus + 1

            # 判断是否为"no-opposite-condition" model
            # 如果小组内局部热感觉值绝对值小于1，且胸、背、腹的Slocal>-1，则opmodel_tell=0，视为"no-opposite-condition" model
            opmodel_tell = 0
            for i in range(1, 15):
                if abs(tsv14[0,i-1]>=1):
                    opmodel_tell = opmodel_tell + 1

            if (tsv14[0,1]<=-1)or(tsv14[0,2]<=-1)or(tsv14[0,3]<=-1):
                opmodel_tell = opmodel_tell + 1;

            # 判断执行步骤2或步骤3
            if (n_minus == 0)or(n_plus == 0)or(opmodel_tell == 0): #执行"no-opposite-condition" model逻辑
            # 判断complaint model 或 gradual model
                if tsv_ascending[0,11]>=2: # 第三大热感觉大于2，对应【"no-opposite-condition" model】-【complaint model】-【warm side】
                    So = 0.5*tsv_ascending[0,13] + 0.5*tsv_ascending[0,11]
                elif tsv_ascending[0,2]<=-2: # 第三小热感觉小于-2【"no-opposite-condition" model】-【complaint model】-【cold side】
                    So = 0.38 * tsv_ascending[0, 0] + 0.62 * tsv_ascending[0, 2]
                elif n_plus == 14: # 【"no-opposite-condition" model】-【gradual model】-【Slightly warm sensations】
                    Interval = 2 / 14
                    n_average = 0
                    for i in range(1, 15):
                        if tsv_ascending[0,14-i]>(2-Interval*(i-2)) :
                            So = So + tsv_ascending[0,14-i]
                            n_average = n_average + 1
                            break
                        else:
                            So = So + tsv_ascending[0, 14 - i]
                            n_average = n_average + 1
                    if n_average == 0:
                        So = 0
                    else:
                        So = So/n_average
                elif n_minus == 14:  #【"no-opposite-condition" model】-【gradual model】-【Slightly cool sensations】
                    Interval = 2 / 14
                    n_average = 0
                    for i in range(1, 15):
                        if tsv_ascending[0,i-1] < (-2+Interval*(i-2)):
                            So = So + tsv_ascending[0,i-1]
                            n_average = n_average + 1
                            break
                        else:
                            So = So + tsv_ascending[0, i - 1]
                            n_average = n_average + 1
                    if n_average == 0:
                        So = 0
                    else:
                        So = So/n_average
                else:
                    So = np.mean(tsv_ascending)
            else: # 执行"opposite-condition" model逻辑
                # 将冷热热感觉分为两组、放入两个矩阵
                tsv_positive = np.zeros((1, n_plus))
                tsv_negative = np.zeros((1, n_minus))
                tsv_p_count = 0
                tsv_n_count = 0
                for i in range(1, 15):
                    if tsv14[0,i-1] >= 0:
                        tsv_p_count = tsv_p_count + 1
                        tsv_positive[0,tsv_p_count-1] = tsv14[0,i-1]
                    else:
                        tsv_n_count = tsv_n_count + 1
                        tsv_negative[0,tsv_n_count-1] = tsv14[0,i-1]
                if n_plus >= n_minus: # 热感觉组为大组
                    # 计算S_overall_bigger_group
                    tsv_ascending = np.sort(tsv_positive, axis=1) # 对热感觉进行排序(升序)，axis = 1代表按行排序
                    if tsv_ascending[0,n_plus-3] >= 2: # 第三大热感觉大于2，对应【complaint model】-【warm side】
                        S_overall_bigger_group = 0.5 * tsv_ascending[0,n_plus-1] + 0.5*tsv_ascending[0,n_plus-3]
                    else: # 第三大热感觉小于2，对应【complaint model】-【Slightly warm sensations】
                        S_overall_bigger_group = 0
                        Interval = 2 / n_plus
                        n_average = 0
                        for i in range(1,n_plus+1):
                            if tsv_ascending[0,n_plus-i] > 2-Interval*(i-2):
                                S_overall_bigger_group = S_overall_bigger_group + tsv_ascending[0,n_plus-i]
                                n_average = n_average + 1
                                break
                            else:
                                S_overall_bigger_group = S_overall_bigger_group + tsv_ascending[0, n_plus - i]
                                n_average = n_average + 1
                        if n_average == 0:
                            S_overall_bigger_group = 0
                        else:
                            S_overall_bigger_group = S_overall_bigger_group/n_average

                    # 计算反向热感觉作用力与整体热感觉
                    if (tsv14[0,1]<=-1)or(tsv14[0,2]<=-1)or(tsv14[0,3]<=-1):
                        So = min(tsv14[0,1],tsv14[0,2],tsv14[0,3]) # 胸、背、腹热感觉值小于-1，全身热感觉值尤其主导
                    else:
                        Individual_force = np.zeros((1, n_minus))
                        deltaS_local = np.zeros((1, 14))
                        If_count = 0
                        for i in range(1, 15):
                            deltaS_local[0,i-1] = tsv14[0,i-1]-tsv140[0,i-1] # deltaS_local(1,i)为各部位供冷/供暖始末局部热感觉变化值
                            if (tsv14[0,i-1]<0)and(deltaS_local[0,i-1]<=-2):
                                If_count = If_count + 1
                                Individual_force[0,If_count-1] = aa.cell(1, i).value*(deltaS_local[0,i-1]-cc.cell(1, i).value)+bb.cell(1, i).value
                            elif(tsv14[0,i-1]<0)and(deltaS_local[0,i-1]>=2):
                                If_count = If_count + 1
                                Individual_force[0, If_count - 1] = aa.cell(3, i).value * (deltaS_local[0, i - 1] - cc.cell(3, i).value) + bb.cell(3, i).value
                            elif(tsv14[0,i-1]<0)and(abs(deltaS_local[0,i-1])<2):
                                If_count = If_count + 1
                                Individual_force[0, If_count - 1] = aa.cell(2, i).value * (deltaS_local[0, i - 1] - cc.cell(2, i).value) + bb.cell(2, i).value

                        If_ascending = np.sort(Individual_force, axis=1) # 对individual force进行排序
                        if n_minus == 1:
                            combined_force = If_ascending[0,0]
                        else:
                            combined_force = If_ascending[0,0] + 0.1*If_ascending[0,1] # 最大的两个individual force用于计算combined force
                        So = S_overall_bigger_group + combined_force
                else: # 冷感觉为大组
                    # 计算S_overall_bigger_group
                    tsv_ascending = np.sort(tsv_negative, axis=1)  # 对热感觉进行排序(升序)，axis = 1代表按行排序
                    if tsv_ascending[0,2] <= -2: # 第三小热感觉小于-2【complaint model】-【cold side】
                        S_overall_bigger_group = 0.38*tsv_ascending[0,0] + 0.62*tsv_ascending[0,2]
                    else: # 第三小热感觉大于-2【complaint model】-【Slightly cool sensations】
                        S_overall_bigger_group = 0
                        Interval = 2/n_minus
                        n_average = 0
                        for i in range(1,n_minus+1):
                            if tsv_ascending[0,i-1]<-2+Interval*(i-2):
                                S_overall_bigger_group = S_overall_bigger_group + tsv_ascending[0,i-1]
                                n_average = n_average + 1
                                break
                            else:
                                S_overall_bigger_group = S_overall_bigger_group + tsv_ascending[0, i - 1]
                                n_average = n_average + 1
                        if n_average == 0:
                            S_overall_bigger_group = 0
                        else:
                            S_overall_bigger_group = S_overall_bigger_group/n_average
                    # 计算反向热感觉作用力与整体热感觉
                    if (tsv14[0,1]<=-1)or(tsv14[0,2]<=-1)or(tsv14[0,3]<=-1):
                        So = min(tsv14[0,1],tsv14[0,2],tsv14[0,3]) # 胸、背、腹热感觉值小于-1，全身热感觉值尤其主导
                    else:
                        Individual_force = np.zeros((1, n_plus))
                        deltaS_local = np.zeros((1, 14))
                        If_count = 0
                        for i in range(1,15):
                            deltaS_local[0, i - 1] = tsv14[0, i - 1] - tsv140[0, i - 1]  # deltaS_local(1,i)为各部位供冷/供暖始末局部热感觉变化值
                            if (tsv14[0,i-1]>0)and(deltaS_local[0,i-1]<=-2):
                                If_count = If_count + 1
                                Individual_force[0,If_count-1] = aa.cell(1, i).value*(deltaS_local[0,i-1]-cc.cell(1, i).value)+bb.cell(1, i).value
                            elif(tsv14[0,i-1]>0)and(deltaS_local[0,i-1]>=2):
                                If_count = If_count + 1
                                Individual_force[0, If_count - 1] = aa.cell(3, i).value * (deltaS_local[0, i - 1] - cc.cell(3, i).value) + bb.cell(3, i).value
                            elif(tsv14[0,i-1]>0)and(abs(deltaS_local[0,i-1])<2):
                                If_count = If_count + 1
                                Individual_force[0, If_count - 1] = aa.cell(2, i).value * (deltaS_local[0, i - 1] - cc.cell(2, i).value) + bb.cell(2, i).value
                        If_ascending = np.sort(Individual_force, axis=1) # 对individual force进行排序
                        if n_plus == 1:
                            combined_force = If_ascending[0,n_plus-1]
                        else:
                            combined_force = If_ascending[0,n_plus-1] + 0.1*If_ascending[0,n_plus-2] #  最大的两个individual force用于计算combined force
                        So = S_overall_bigger_group + combined_force
            # 计算局部热舒适
            for i in range(1,17):
                if So < 0:
                    a[0,i-1] = (-4-(c6.cell(1, i).value + c71.cell(1, i).value*abs(So)))/((-4+c31.cell(1, i).value*abs(So)+c8.cell(1, i).value)**n.cell(1, i).value)-(-4-(c6.cell(1, i).value+c71.cell(1, i).value*abs(So)))/((4+c31.cell(1, i).value*abs(So)+c8.cell(1, i).value)**n.cell(1, i).value)
                    right_slope[0,i-1] =  (-4-(c6.cell(1, i).value + c71.cell(1, i).value*abs(So)))/((4+c31.cell(1, i).value*abs(So)+c8.cell(1, i).value)**n.cell(1, i).value)
                    offset[0,i-1] = c31.cell(1, i).value*abs(So)+c8.cell(1, i).value
                    maxcomfort[0,i-1] = c6.cell(1, i).value+c71.cell(1, i).value*abs(So)
                    tcv[0,i-1] = (a[0,i-1]/(np.exp(25*(tsv[0,i-1]+offset[0,i-1]))+1) + right_slope[0,i-1])*((tsv[0,i-1]+offset[0,i-1])*n.cell(1, i).value)+maxcomfort[0,i-1]
                else:
                    a[0,i-1] = (-4-(c6.cell(1, i).value + c72.cell(1, i).value*abs(So)))/((-4+c32.cell(1, i).value*abs(So)+c8.cell(1, i).value)**n.cell(1, i).value)-(-4-(c6.cell(1, i).value+c72.cell(1, i).value*abs(So)))/((4+c32.cell(1, i).value*abs(So)+c8.cell(1, i).value)**n.cell(1, i).value)
                    right_slope[0, i - 1] = (-4 - (c6.cell(1, i).value + c72.cell(1, i).value * abs(So)))/((4 + c32.cell(1, i).value * abs(So) + c8.cell(1, i).value) ** n.cell(1, i).value)
                    offset[0, i - 1] = c32.cell(1, i).value * abs(So) + c8.cell(1, i).value
                    maxcomfort[0, i - 1] = c6.cell(1, i).value + c72.cell(1, i).value * abs(So)
                    tcv[0, i - 1] = (a[0, i - 1] / (np.exp(25 * (tsv[0, i - 1] + offset[0, i - 1])) + 1) + right_slope[0, i - 1]) * ((tsv[0, i - 1] + offset[0, i - 1]) * n.cell(1, i).value) + maxcomfort[0, i - 1]

            # 计算整体热舒适
            # 此处仅保留手脚中，不舒适性较高的热舒适值
            tcv14 = np.zeros((1, 14))
            for i in range(1, 9):
                tcv14[0, i - 1] = tcv[0, i - 1]

            for i in range(10, 14):
                tcv14[0, i - 1] = tcv[0, i]

            # 保留不舒适性较差的手部热舒适值
            if tcv[0,8]<tcv[0,9]:
                tcv14[0,8] = tcv[0,8]
            else:
                tcv14[0,8] = tcv[0,9]

            # 保留不舒适性较差的脚部热舒适值
            if tcv[0,14] < tcv[0,15]:
                tcv14[0,13] = tcv[0,14]
            else:
                tcv[0,13] = tcv[0,15]

            tcv_ascending = np.sort(tcv14,axis=1)

            tcvo = (tcv_ascending[0,0] + tcv_ascending[0,1])/2 # 【Rule 1】
            # tcvo =  (tcv_ascending[0,0] + tcv_ascending[0,1] + tcv_ascending[0,13])/3 # 【Rule 2】对应瞬态环境/有调节行为场景

            tout[time-time_pre_treatment, 1] = t[0, 0]  # 取9点法+t65+平均皮温度
            tout[time-time_pre_treatment, 2] = t[0, 1]
            tout[time-time_pre_treatment, 3] = t[0, 2]
            tout[time-time_pre_treatment, 4] = t[0, 3]
            tout[time-time_pre_treatment, 5] = t[0, 4]
            tout[time-time_pre_treatment, 6] = t[0, 6]
            tout[time-time_pre_treatment, 7] = t[0, 8]
            tout[time-time_pre_treatment, 8] = t[0, 10]
            tout[time-time_pre_treatment, 9] = t[0, 12]
            tout[time-time_pre_treatment, 10] = t[0, 14]
            tout[time-time_pre_treatment, 11] = bc[0, 0]
            tout[time-time_pre_treatment, 12] = tmsk
            tout[time-time_pre_treatment, 13] = dt65
            tout[time-time_pre_treatment, 14] = hf65
            tout[time-time_pre_treatment, 15] = t65
            # c_head_core =c.cell(1, 1).value

            ## 参数输出 ##
            #输出时间值
            sheet1.write(time, 0, time-time_pre_treatment)
            sheet2.write(time, 0, time-time_pre_treatment)
            sheet3.write(time, 0, time-time_pre_treatment)
            #输出平均皮肤温度
            sheet1.write(time, 1, tmsk)
            #输出各节段皮肤温度
            for i in range(1, 17):
                sheet1.write(time, i+1, t[3, i - 1])
            #输出腹部核心温度
            sheet1.write(time, 18, t[0, 3])
            # 输出整体热感觉值
            sheet2.write(time, 1, So)
            # 输出局部热感觉值
            for i in range(1, 17):
                sheet2.write(time, i + 1, tsv[0, i - 1])
            # 输出整体热舒适值
            sheet3.write(time, 1, tcvo)
            # 输出局部热舒适值
            for i in range(1, 17):
                sheet3.write(time, i + 1, tcv[0, i - 1])


            #时间更新
            time = time + 1
        #tset = pr1.sheets()[6]
        #tbody= sheet1.row_values(time)
        #sheet11.write(cid, , tbody)

        os.makedirs(savepath + '\\' + str(cid) + ' _output0530',exist_ok=True)
        T_body.save(savepath  + '\\' + str(cid) + ' _output0530/'+ str(cid) + '_T_body.xls')
        TSV.save(savepath + '\\'  + str(cid) + ' _output0530/TSV.xls')
        TCV.save(savepath + '\\'  + str(cid) + ' _output0530/TCV.xls')
        e3.delete(0,END)
        e4.delete(0,END)
        e3.insert(0,tair[0][0])
        e4.insert(0,c65)
    tk.messagebox.askokcancel(title='成功', message='计算成功！')
# 定义路径选择函数
def filec0():
    global pr0,ll1
    # 选择路径
    path_ = askopenfilename()
    # 赋值全局变量
    pr0 = path_
    # 显示在右侧白框中
    ll1.delete(0,END)
    ll1.insert(0,pr0)
def filec1():
    global pr1,ll2
    path_ = askopenfilename()
    pr1 = path_
    ll2.delete(0, END)
    ll2.insert(0, pr0)
def filec2():
    global pr2,ll3
    path_ = askopenfilename()
    pr2 = path_
    ll3.delete(0, END)
    ll3.insert(0, pr0)
def filec3():
    global pr3,ll4
    path_ = askopenfilename()
    pr3 = path_
    ll4.delete(0, END)
    ll4.insert(0, pr0)
def filec4():
    global pr4,ll5
    path_ = askdirectory()
    pr4 = path_
    ll5.delete(0, END)
    ll5.insert(0, pr0)
root = Tk()
root.geometry('800x520')
pr0 = ''
pr1 = ''
pr2 = ''
pr3 = ''
pr4 = ''
l1 = Label(root, text='预处理时间:')
l1.place(x=500, y=30)
e1 = Entry(root)
e1.place(x=500, y=60)
l2 = Label(root, text='t65:')
l2.place(x=500, y=130)
e2 = Entry(root)
e2.place(x=500, y=160)
l3 = Label(root, text='tair:')
l3.place(x=500, y=230)
e3 = Entry(root)
e3.place(x=500, y=260)
l4 = Label(root, text='c65:')
l4.place(x=500, y=330)
e4 = Entry(root)
e4.place(x=500, y=360)
ll1 = Entry(root,width=46)
ll1.place(x=150,y=40)
ll2 = Entry(root,width=46)
ll2.place(x=150,y=140)
ll3 = Entry(root,width=46)
ll3.place(x=150,y=240)
ll4 = Entry(root,width=46)
ll4.place(x=150,y=340)
ll5 = Entry(root,width=46)
ll5.place(x=150,y=440)
# 为每个按钮绑定函数
Button(root, width=13, height=2, text='输入文件1', command=filec0).place(x=30, y=30)
Button(root, width=13, height=2, text='输入文件2', command=filec1).place(x=30, y=130)
Button(root, width=13, height=2, text='输入文件3', command=filec2).place(x=30, y=230)
Button(root, width=13, height=2, text='输入文件4', command=filec3).place(x=30, y=330)
Button(root, width=13, height=2, text='保存路径', command=filec4).place(x=30, y=430)
# 计算按钮绑定主函数，传递选定的各个值
Button(root, width=13, height=2, text='计算', command=lambda :f(pr0,pr1,pr2,pr3,pr4,int(e1.get()),float(e2.get()))).place(x=500, y=430)
l1 = Label(root)
l1.place(x=150, y=20)
root.mainloop()
# print (tout[5, 1:16])
# print (tout[10, 1:16])
# print (tout[30, 1:16])
#
# print (tair)
# print (c65)
