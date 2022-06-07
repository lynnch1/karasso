from interact_with_DB import interact_db

class db_coords:

    def change_name(self, name, x_pos, y_pos, floor_name):  # put application's code here
        query = "update coordinates set name='%s' WHERE x_pos='%s' AND y_pos='%s' AND floor_name='%s';" % (
           name, x_pos, y_pos, floor_name)
        interact_db(query=query, query_type='commit')
        return True

    def change_location(self, x_pos, y_pos, name, floor_name):  # put application's code here
        print(x_pos, y_pos)
        query = "update coordinates set x_pos='%s' where name='%s' AND floor_name='%s';" % (
            x_pos, name, floor_name)
        interact_db(query=query, query_type='commit')
        query1 = "update coordinates set y_pos='%s' where name='%s' AND floor_name='%s';" % (
            y_pos, name, floor_name)
        interact_db(query=query1, query_type='commit')
        return True

    def get_Existing_floor(self):
        query = "select * from floors"
        floor = interact_db(query=query, query_type='fetch')
        return floor

    def get_floor_details(self, floor_name):
        query = "select * from floors where floor_name='%s';" % (
            floor_name)
        floor_details = interact_db(query=query, query_type='fetch')
        return floor_details


    def get_Existing_locations(self, floor_name):
        query = "select * from coordinates where floor_name='%s';" % (
            floor_name)
        locations = interact_db(query=query, query_type='fetch')
        return locations

    def check_exist_coordinates(self, x_pos, y_pos, floor_name):
        check_exist = "SELECT x_pos, y_pos FROM coordinates WHERE floor_name='%s' AND x_pos='%s' AND y_pos='%s' ;" % (
            floor_name, x_pos, y_pos)
        existing = interact_db(query=check_exist, query_type='fetch')
        print(len(existing))
        if len(existing) == 0:
            return False
        else:
            return True

    def check_exist_name(self, name, floor_name):
        check_exist = "SELECT name FROM coordinates WHERE floor_name='%s' AND name='%s' ;" % (
            floor_name,name)
        existing = interact_db(query=check_exist, query_type='fetch')
        print(len(existing))
        if len(existing) == 0:
            return False
        else:
            return True





db_coords = db_coords()