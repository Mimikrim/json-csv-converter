import JSON_to_CSV
import CSV_to_JSON
import time

#start_time = time.time()
#JSON_to_CSV.json_to_csv_without_id(["ID", "name", "animal ID", "animal", "service"], "common_json_file.json", "test_common_json_file.csv",";")
#print("---%s seconds ---" % (time.time() - start_time))

#start_time = time.time()
#JSON_to_CSV.json_to_csv_without_id(["pk", "model", "fields/codename", "fields/name", "fields/content_type"], "uncommon_json_file.json", "test_uncommon_json_file.csv",";")
#print("---%s seconds ---" % (time.time() - start_time))

#start_time = time.time()
#JSON_to_CSV.json_to_csv_with_id(["names_of_animal_owners", "animals"],"File_with_attachments_with_ID.json", "File_with_attachments_with_ID.csv", ";")
#print("---%s seconds ---" % (time.time() - start_time))

start_time = time.time()
CSV_to_JSON.common_file("common_csv_file.csv", "test_common_csv_file.json", None, None)
print("---%s seconds ---" % (time.time() - start_time))


