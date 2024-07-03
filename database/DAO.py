from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getProvider():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct Provider 
                        from nyc_wifi_hotspot_locations nwhl """
        cursor.execute(query, )
        for row in cursor:
            result.append(row["Provider"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(provider):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select  distinct  Location 
                    from nyc_wifi_hotspot_locations nwhl 
                    where Provider = %s"""
        cursor.execute(query, (provider,) )
        for row in cursor:
            result.append(row["Location"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(soglia):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """"""
        cursor.execute(query, (soglia,))
        for row in cursor:
            result.append((row["v1"], row["v2"], row["peso"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAll(provider):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT n1.Location as n1Loc, n2.Location as n2Loc, avg(n1.Latitude) as n1Lat, avg(n1.Longitude) as n1Long, avg(n2.Latitude) as n2Lat, avg(n2.Longitude) as n2Long
                    FROM nyc_wifi_hotspot_locations n1 , nyc_wifi_hotspot_locations n2 
                    WHERE n1.Provider = n2.Provider 
                    and n1.Provider = %s
                    and n1.Location < n2.Location 
                    GROUP by n1.Location, n2.Location"""
        cursor.execute(query, (provider,) )
        for row in cursor:
            result.append((row["n1Loc"], row["n1Lat"], row["n1Long"],row["n2Loc"], row["n2Lat"], row["n2Long"]))

        cursor.close()
        conn.close()
        return result


