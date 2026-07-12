# --- THE IDENTITY GLITCH ---
# The archive has corrupted these profiles.
# Types are wrong. Repair them.

# POET
poet_name = str(123)  # this value should be a string
poet_age = int("29") # here we are using string instead of number
poet_is_published = "True" == "True" # here is not a boolean is a string value - for the comparison here it hold an boolean value

# SCIENTIST
scientist_height = float("1.78") # float as string
scientist_papers_count = int("47")# whole number as string 
scientist_is_alive = bool(0) # idk because even zero sometimes can be a boolean

# TIME TRAVELER
traveler_birth_year = int("2147") # here we are using string instead of int 
traveler_speed = float("299792.458")# here string instead of float numbers 
traveler_has_paradox = bool(1) #  the same for what before it can be true
traveler_id = 90210 # true
