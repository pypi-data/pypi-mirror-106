import json
import pymssql

class sqlQuery:

    def tableGoods(self, firstClassCode, machineId):
        try:
            conn = pymssql.connect(host="10.4.1.143", user='lcms_dev', password='lccms!!lem0601', database='LCMS', charset='EUC-KR')
            cursor = conn.cursor()
            
            sql = "SELECT "
            sql = sql + "[FirstClassCode], "
            sql = sql + "[MachineID], "
            sql = sql + "[MngNum], "
            sql = sql + "[Goods1Num], "
            sql = sql + "[SecondClassCode], "
            sql = sql + "[ThirdClassCode], "
            sql = sql + "[BmName], "
            sql = sql + "[BmPassword], "
            sql = sql + "[InstallAddr1], "
            sql = sql + "[InstallAddr2], "
            sql = sql + "[InstallLat], "
            sql = sql + "[InstallLng], "
            sql = sql + "[serialNo], "
            sql = sql + "[typeCode], "
            sql = sql + "[fullMachineID] "
            sql = sql + "FROM [dbo].[BendingMachineBasicInfo] Where firstClassCode =" + "'" + firstClassCode + "' And machineId =" + "" + machineId + ""
            
            print(sql)
            cursor.execute(sql)
            row_headers=[x[0] for x in cursor.description] #this will extract row headers
            #json.dumps(data, indent=5, sort_keys=True, ensure_ascii=False)
            #print(data)
            row = cursor.fetchone()
            json_header = []

            #######################################################################
            vendMachineInfo_firstClassCodes = []
            vendMachineInfo_machineId = []
            vendMachineInfo_mngNum = []
            vendMachineInfo_goods1Num = []
            vendMachineInfo_secondClassCode = []
            vendMachineInfo_thirdClassCode = []
            vendMachineInfo_bmName = []
            vendMachineInfo_bmPassword = []
            vendMachineInfo_installAddr1 = []
            vendMachineInfo_installAddr2 = []
            vendMachineInfo_installLat = []
            vendMachineInfo_installLng = []
            vendMachineInfo_serialNo = []
            vendMachineInfo_typeCode = []
            vendMachineInfo_fullMachineID = []
            #######################################################################

            json_goodsCodes = []
            json_goodsNames = []
            result = {}

            while row:
                vendMachineInfo_firstClassCodes.append(str(row[0]))
                vendMachineInfo_machineId.append(str(row[1]))
                vendMachineInfo_mngNum.append(str(row[2]))
                vendMachineInfo_goods1Num.append(str(row[3]))
                vendMachineInfo_secondClassCode.append(str(row[4]))
                vendMachineInfo_thirdClassCode.append(str(row[5]))
                vendMachineInfo_bmName.append(str(row[6]))
                vendMachineInfo_bmPassword.append(str(row[7]))
                vendMachineInfo_installAddr1.append(str(row[8]))
                vendMachineInfo_installAddr2.append(str(row[9]))
                vendMachineInfo_installLat.append(str(row[10]))
                vendMachineInfo_installLng.append(str(row[11]))
                vendMachineInfo_serialNo.append(str(row[12]))
                vendMachineInfo_typeCode.append(str(row[13]))
                vendMachineInfo_fullMachineID.append(str(row[14]))
                row = cursor.fetchone()
            i = 0            
           
            for list in range(1,2):
                list_tmp = []
                list_tmp2 = []
                for json_firstClassCode in vendMachineInfo_firstClassCodes:
                    list_tmp.append({
                        "firstClassCode" :vendMachineInfo_firstClassCodes[i], 
                        "machineId" :vendMachineInfo_machineId[i], 
                        "mngNum" :vendMachineInfo_mngNum[i],
                        "goods1Num" :vendMachineInfo_goods1Num[i],
                        "secondClassCode" :vendMachineInfo_secondClassCode[i],
                        "thirdClassCode" :vendMachineInfo_thirdClassCode[i],
                        "bmName" :vendMachineInfo_bmName[i],
                        "bmPassword" :vendMachineInfo_bmPassword[i],
                        "installAddr1" :vendMachineInfo_installAddr1[i],
                        "installAddr2" :vendMachineInfo_installAddr2[i],
                        "installLat" :vendMachineInfo_installLat[i],
                        "installLng" :vendMachineInfo_installLng[i],
                        "serialNo" :vendMachineInfo_serialNo[i],
                        "typeCode" :vendMachineInfo_typeCode[i],
                        "fullMachineID" :vendMachineInfo_fullMachineID[i]
                        })
                    list_tmp2.append({
                        "firstClassCode" :vendMachineInfo_firstClassCodes[i], 
                        "machineId" :vendMachineInfo_machineId[i], 
                        "mngNum" :vendMachineInfo_mngNum[i]})
                    i = i + 1
                
                result = {"resultCode":"S", "basicInforList":list_tmp, "uiInfoList":list_tmp2}

                # result[list] = {"basicInforList":list_tmp}
            print(json.dumps(result, indent=4))
            return result

        except Exception as ex:
            print(ex)


    def login(self, firstClassCode, machineId):
        try:
            conn = pymssql.connect(host="10.4.1.143", user='lcms_dev', password='lccms!!lem0601', database='LCMS', charset='EUC-KR')
            cursor = conn.cursor()
            
            sql = "SELECT "
            sql = sql + "count(*) "
            sql = sql + "FROM [dbo].[BendingMachineBasicInfo] Where firstClassCode =" + "'" + firstClassCode + "' And machineId =" + "" + machineId + ""

            cursor.execute(sql)
            row = cursor.fetchone()
            count = row[0]
            
            if count == 0:
                result = False
            else:
                result = True
            return result

        except Exception as ex:
            print(ex)