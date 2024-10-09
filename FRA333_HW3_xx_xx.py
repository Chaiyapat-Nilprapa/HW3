# file สำหรับเขียนคำตอบ
# ในกรณีที่มีการสร้าง function อื่น ๆ ให้ระบุว่า input-output คืออะไรด้วย
'''
ชื่อ_รหัส(ธนวัฒน์_6461)
1. ชัยภัทร_6516
2. ธรา_6529
3.
'''
import numpy as np
import math
import HW3_utils as FKHW3

#=============================================<คำตอบข้อ 1>======================================================#
#code here
def endEffectorJacobianHW3(q:list[float])->list[float]:
     # Input:
    # q: เวกเตอร์ Joint Configuration ขนาด 3x1
    # Output:
    # J_e: Jacobian Matrix ขนาด 6x3

    # เรียกใช้ฟังก์ชัน Forward Kinematics
    R, P, R_e, p_e = FKHW3(q)

    # สร้างเมทริกซ์ Jacobian ขนาด 6x3
    J_e = np.zeros((6, 3))

    # ตำแหน่งเฟรมในพิกัดหลัก (Frame 0)
    p_0_0 = P[:, 0]  # ตำแหน่งของเฟรม 0
    p_0_1 = P[:, 1]  # ตำแหน่งของเฟรม 1
    p_0_2 = P[:, 2]  # ตำแหน่งของเฟรม 2
    p_0_e = p_e      # ตำแหน่งของ End Effector

    # แกนการหมุนของข้อต่อในเฟรมหลัก
    z0 = np.array([0, 0, 1])  # แกน z ของเฟรม 0
    z1 = R[:, 2, 0]           # แกน z ของเฟรม 1
    z2 = R[:, 2, 1]           # แกน z ของเฟรม 2

    # คำนวณ J_v
    J_v1 = np.cross(z0, (p_0_e - p_0_0))
    J_v2 = np.cross(z1, (p_0_e - p_0_1))
    J_v3 = np.cross(z2, (p_0_e - p_0_2))

    # คำนวณ J_omega
    J_w1 = z0
    J_w2 = z1
    J_w3 = z2

    # ใส่ค่าในเมทริกซ์ Jacobian
    J_e[0:3, 0] = J_v1
    J_e[0:3, 1] = J_v2
    J_e[0:3, 2] = J_v3

    J_e[3:6, 0] = J_w1
    J_e[3:6, 1] = J_w2
    J_e[3:6, 2] = J_w3
    print(J_e)
    return J_e

    pass
#==============================================================================================================#
#=============================================<คำตอบข้อ 2>======================================================#
#code here
def checkSingularityHW3(q:list[float])->bool:
    pass
#==============================================================================================================#
#=============================================<คำตอบข้อ 3>======================================================#
#code here
def computeEffortHW3(q:list[float], w:list[float])->list[float]:
    pass
#==============================================================================================================#