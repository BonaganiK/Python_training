work_order = {
    "code": "R000000995",
    "description": "Replace, lubricate bearing, align component",
    "staff": {
        "staffMemberId": 0,
        "staffMemberCode": "UNKNOWN",
        "staffMemberContactDetailFullName": "A UNKNOWN",
        "staffMemberDefaultResourceTradeTradeId": 0,
        "staffMemberDefaultResourceTradeTradeCode": "UNKNOWN",
        "staffMemberDefaultResourceTradeTradeDescription": "UNKNOWN"
    }
}

work_order2 = {
    "code": "R000000995",
    "description": "Replace, lubricate bearing, align component"
}

  # def get_workorder_data(work_order_record, field_name):
  # return work_order_record.get(field_name,)
     
  # print(get_workorder_data(work_order, "code"))
  # print(get_workorder_data(work_order, "description"))

  # assign_staff_member(work_order2) <- will fail

  # Functions with Parameters

  # function named 'get_work_order_code' that takes a dictonery work_order_record and as input.
  # it update the value of the code key from the dictonary using 'get' method
  # if the key is not found in the dictonary return value "No code"

def get_work_order_code(work_order_record):
    return work_order_record.get("code", "No code") # JHR: yes, but you can actually just leave out the "No code" just return the None it's fine

  # function named "get_work_order_code" that takes a dictonery 'work_order_record' and as input.
  # it update the value of the description key from the dictonary using 'get' method.
  # if the key is not found in dictonary return value 'No description'

def get_work_order_description(work_order_record):
    return work_order_record.get("description", "No description") # JHR: same as above

  # the function named 'assign_staff_member' that takes a 'staff_id' and work_order_record' as a dictionary as input.
  #It updates the value of 'staffMemberId' in the nested dictionary work_order_record["staff"] with the provided staff_id

def assign_staff_member(staff_id, work_order_record): # JHR: keep the same order (consistancy) work_order_record, staff_id
    
    if "staffMemberId" in work_order_record["staff"]:
        work_order_record["staff"]["staffMemberId"] = staff_id 
    else:
        work_order_record["staff"]["staffMemberId"] = 0

       


    # JHR: what if staff does not exist??
    # JHR: if there is no staff what is the expected business rules ? do I create one ? or just leave it ?


  # Implement a function process_work_order that depends on the results of other functions (get_work_order_code and get_work_order_description
  # the function named 'process_work_order' that takes a 'work_order_record' as dictionary input.
  # then we call get_work_order_code and get_work_order_description functions to print the value of the code and description of the work order

def process_work_order(work_order_record):

    code = get_work_order_code(work_order_record)
    description = get_work_order_description(work_order_record)

    print("Work Order Code:", code)
    print("Work Order Description:", description)

  # Conditional Statements:
  # Utilize conditional statements within the process_work_order function to determine the assignment of a staff member based on the work order code.
  # For instance, if the code starts with "R", assign a certain staff member; otherwise, assign another.

    if code.startswith("R"): # JHR: be careful of your indentation, it does not match
      assign_staff_member(1020, work_order_record)
    else:
      assign_staff_member(2020, work_order_record)

  #Output Generation:
  #Using an f-string, create a sentence that includes details of the work order such as its code, description, and the assigned staff member ID.

def generate_work_order_sentance(work_order_record):
    code = work_order_record["code"]
    description = work_order_record["description"]
    staff_member_id = work_order_record['staff']['staffMemberId'] # JHR: what if the staff does not exist?
    sentance = (f"Work Order Code: {code}, Description: {description}, Staff Member Id: {staff_member_id}")
    print(sentance)

process_work_order(work_order)
generate_work_order_sentance(work_order)


