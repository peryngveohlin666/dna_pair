from random import randrange


class Pair:
    def __init__(self):
        self.yes_no_dict = {"yes": True, "y": True, "Y": True, "no": False, "n": False, "Y": False}
        self.nucleotide_dict = {"a": "a", "t": "t", "g": "g", "c": "c",
                                "A": "a", "T": "t", "G": "g", "C": "c"}
        self.pairing_dict = {"a": "t", "t": "a", "g": "c", "c": "g"}
        self.random_nucleotides = ["a", "t", "g", "c"]
        self.mutations = None
        self.nucleotides = []
        self.paired_nucleotides = []
        self.mutation_prompt()
        self.enter_nucleotides()
        self.complementary_pairing()
        print(self)

    def __str__(self):
        def append(list_of_chars):
            new_str = ""
            for character in list_of_chars:
                new_str += character
            return new_str

        return (append(self.nucleotides) + "\n" + append(self.paired_nucleotides))

    def mutation_prompt(self):
        while self.mutations is None:
            try:
                self.mutations = self.yes_no_dict[input("Would you like there to be mutations? (y/n)\n")]
            except KeyError:
                print("Please enter a valid answer")

    def enter_nucleotides(self):
        while not self.nucleotides:
            try:
                nucleotide_string = input("Please enter a group of nucleotides (a/t/g/c/A/T/G/C)")
                for nucleotide in nucleotide_string:
                    self.nucleotides.append(self.nucleotide_dict[nucleotide])
            except KeyError:
                self.nucleotides = []
                print("invalid prompt")

    def complementary_pairing(self):
        if not self.mutations:
            for nucleotide in self.nucleotides:
                self.paired_nucleotides.append(self.pairing_dict[nucleotide])
        else:
            for nucleotide in self.nucleotides:
                random_chance = randrange(0, 100)
                if random_chance != 7:
                    self.paired_nucleotides.append(self.pairing_dict[nucleotide])
                else:
                    self.paired_nucleotides.append(self.pairing_dict[self.random_nucleotides[randrange(0, 3)]])
