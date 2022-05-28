from turtle import ScrolledCanvas

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        
    # methods
    def change_name(self, new_name):
        self.new_name = new_name
        return new_name
        
    def change_age(self, new_age):
        self.new_age = int(new_age)
        return new_age

    def add_track(self, new_track):
        self.new_track = new_track
        self.tracks.append(new_track)
        return self.tracks
    
    def get_score(self):
        return self.score
        
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print("Name: {}".format(Bob.change_name("Peter"))) 
print("Age: {}".format(Bob.change_age(34)))
print("Tracks: {}".format(Bob.add_track("UI/UX")))
print("Score: {}".format(Bob.get_score()))

