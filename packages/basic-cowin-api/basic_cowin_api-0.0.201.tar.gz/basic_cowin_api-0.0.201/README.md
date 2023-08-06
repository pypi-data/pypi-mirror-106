# Basic Cowin API 

Python API wrapper for CoWin API, for details visit https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2


Basic Example:

```python
from cowin_api import CoWin

cw = CoWin()

# Returns the details of states
result = cw.get_state_list()
print(result)

# Returns the details of districts for a given state
# in this case with state_id 2
result = cw.get_districts_list(2)
print(result)

# Returns the details of districts for a given state with 
# open slots for age group 45 and free payment for vaccination.
 
result = cw.check_by_district_id(district=651, age=45, payment="free")
print(result)

# Returns the details of slots available in area with 
# pincode 462003
result = cw.check_by_pincode(462003)
print(result)

# Returns the details of slots available in area with 
# district id 650 -> obtained from `get_districts_list`
result = cw.check_by_district_id(650)
print(result)
```

# Install

`pip install basic_cowin_api`


# Notes:

- The API's of CoWin MAY NOT work from servers outside of India.
- Payment Options are: `any`, `free` and `paid`.
- Age Options are: `18` and `45`

---

# Roadmap:

- [x] Add a filter to search by age group of 18-45 and 45+
- [x] Add a filter for free and paid vaccine
- [ ] Search for multiple pin codes
- [ ] Search for multiple districts
- [ ] Add a filter based of vaccine
- [ ] Implement test cases

---

# License:

GNU 3