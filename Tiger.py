# Import the Animal class from the Animal module
from Animal import Animal

class Tiger(Animal):
    # create a static class variable to keep track of the number of tigers created
    numOfTiger = 0

    # Create the hyena sound
    tiger_sound = ["Meow", "Meeoow", "MEOW", "mmmeoww"]


    # Create a list of tiger names.
    list_of_tiger_names = []

    file_path = r'C:\Users\caleb\OneDrive\Desktop\Midterm_Program_Python_2024\animalNames.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num == 15:
                list_of_tiger_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, age="a_age", name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex",
                 weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):
        # Increment the static variable numOfHyenas when a new Tiger object is created
        Tiger.numOfTiger += 1

        # Call the constructor of the parent class (Animal) with 'Tiger' as the species
        super().__init__("tiger", age, name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)

        def make_sound(self):
            return self.tiger_sound


    # the tiger object will call this method to get an unused tiger name. pop() will remove the first element from
    #   the list_of_tiger_names[]
    def get_tiger_name(self):
        return self.list_of_tiger_names.pop(0)


