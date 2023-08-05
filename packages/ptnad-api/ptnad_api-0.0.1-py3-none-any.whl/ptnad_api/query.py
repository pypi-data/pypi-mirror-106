import json

class BQLQuery:
    def __init__(self, data_provider, selected_fields, entity_class, time_range, nad_filter, limit=None):
        self.selected_fields = selected_fields
        self.entity_class = entity_class
        self.data_provider = data_provider
        self.time_range = time_range
        self.nad_filter = nad_filter
        self.limit = limit

    def get_query(self):
        #class_fields = set(self.entity_class.get_all_fields())
        #current_fields_set = set(self.selected_fields)
        #if current_fields_set.issubset(class_fields):            
        return "SELECT " + ", ".join(self.selected_fields) + \
                   " FROM " + self.entity_class.get_class() + \
                  F" WHERE (end >= {self.time_range.start} AND end <= {self.time_range.end})" + \
                  (F" and ({self.nad_filter})" if self.nad_filter != None else "") + \
                  (f" LIMIT {self.limit}" if self.limit is not None else "")
        #else:
        #    return None

    def get_entity_from_list(self, values):
        if len(self.selected_fields) != len(values):
            raise Exception("Value count missmatch")
        kv = dict()
        for i in range(len(values)):
            kv.update({self.selected_fields[i]:values[i]})
        return self.entity_class.from_dict(kv)

    def execute(self, logger):
        results = []
        for row in self.data_provider.execute_query(logger, self):
            results.append(self.get_entity_from_list(row))
        return results