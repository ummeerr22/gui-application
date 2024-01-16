import random
import requests
import html
import tkinter as tk
from tkinter import messagebox



def get_Q(amount: int, category: int) -> list:
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    response_json = response.json()
    return response_json.get("results", [])

class Startframe(tk.Frame):
    def __init__(self, master, app):
        tk.Frame.__init__(self, master, bg="lightblue")
        self.app = app
        self.pack()
        self.create_widgets()

    def create_widgets(self):
    
        head1_label = tk.Label(self, text=" Random Quiz ", font=("Fixedsys", 70), bg="lightblue",fg="#FF004D")
        head1_label.pack(pady=50)

        welcome_label = tk.Label(self, text="Welcome to the Quiz Application", font=("Fixedsys", 16), bg="lightblue" )
        welcome_label.pack(pady=20)

        start_button = tk.Button(self, text="          Start Quiz          ", command=self.app.display_intro_frame, bg="#65B741")
        start_button.pack(padx=5, pady=10)

class Introductionframe(tk.Frame):
    def __init__(self, master, app):
        tk.Frame.__init__(self, master, bg="lightblue")
        self.app = app
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        head2_label = tk.Label(self, text=" Introduction ", font=("Fixedsys", 18), bg="lightblue")
        head2_label.pack(pady=10)

        info_label = tk.Label(self, text=" shfbvisrbvkshbvkshvbfk ", font=("Comic Sans MS,", 14), bg="#0F2167", fg="#4CB9E7")
        info_label.pack(pady=10)

        start_quiz_button = tk.Button(self, text="          Start Quiz          ", command=self.app.load_question, bg="#65B741")
        start_quiz_button.pack(padx=5,pady=10)

class QuizGUI(tk.Frame):
    def __init__(self, master, amount, category):
        tk.Frame.__init__(self, master, bg="lightblue")
        self.master = master
        self.amount = amount
        self.category = category
        self.question_pool = get_Q(self.amount, self.category)
        self.current_question_index = 0
        self.score = 0
        self.pack()
        self.display_start_frame()
       

    def display_start_frame(self):
        self.start_window = Startframe(self.master, self)

    def display_intro_frame(self):
        self.start_window.destroy()
        self.intro_window = Introductionframe(self, self)

    def load_question(self):
        self.intro_window.destroy()
        self.question_label = tk.Label(self, bg="lightblue", font=("Fixedsys", 16), text="", wraplength=400)
        self.question_label.pack(pady=30)

        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(self, text="", command=lambda idx=i: self.handle_choice(idx), bg="#9BB8CD" )
            button.pack(padx=5, pady=10)
            self.choice_buttons.append(button)

        self.load_next_question()

    def shuffle_choices(self, choices: list) -> list:
        shuffled_choices = random.sample(choices, len(choices))
        return shuffled_choices
    
    def show_final_score(self):
        self.question_label.grid_remove()
        for button in self.choice_buttons:
            button.grid_remove()

        final_score_label = tk.Label(self, font=("Fixedsys",40), fg="#FF004D", bg="lightblue", text=f"Final Score: {self.score}")
        final_score_label.pack(pady=40)


    def load_next_question(self):
        if self.current_question_index < len(self.question_pool):
            question = self.question_pool[self.current_question_index]
            question_text = html.unescape(question.get("question", ""))
            self.question_label.config(text=question_text)
            choices = question.get("incorrect_answers", [])
            choices.append(question.get("correct_answer", ""))
            shuffled_choices = self.shuffle_choices(choices)
            for i in range(4):
                self.choice_buttons[i].config(text=html.unescape(shuffled_choices[i]))
        else:
            messagebox.showinfo("Quiz wrapped up! You've successfully finished it.")
            self.show_final_score()

    def handle_choice(self, idx):
        correct_choice_text = html.unescape(self.question_pool[self.current_question_index].get("correct_answer", ""))
        user_choice_text = self.choice_buttons[idx].cget("text")
        if user_choice_text == correct_choice_text: 
            self.score += 1
            messagebox.showinfo("Result", f"Spot on! You nailed it!  your answer: {correct_choice_text}")
           
        else:
            messagebox.showinfo("Result", f"Oops! The correct one is: {correct_choice_text}")
        self.current_question_index += 1
        self.load_next_question()



if __name__ == "__main__":
    amount = 10
    category = 11
    root = tk.Tk()
    root.config(bg="lightblue")
    root.title("Quiz Application")
    root.geometry("700x500+100+100")
    app = QuizGUI(root, amount, category)
    root.mainloop()
