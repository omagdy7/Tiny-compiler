from manim import *
import re

regex_input = input("Please enter your input: ")
whitespace = r"\s"
letter = r"[a-zA-Z]"
num = r"[0-9]"
right = "right"
left = "left"
down = "down"
up = "up"

def reset_ar(arrows):
    for arrow in arrows:
        arrow.set_color(WHITE)

def reset_cir(circs):
    for circle in circs:
        circle.set_stroke(WHITE).set_fill(WHITE, opacity=0)
# Function that centers text in the middle of a circle
def center_text(txt, circ):
    return Text(txt).move_to(circ.get_center()).scale(0.6)
# Function that draws arrows between circs based on input
def drawArrows(cir1, cir1_side, cir2, cir2_side, ang, tip):
    if(cir1_side == "right" and cir2_side == "right"):
        return CurvedArrow(angle=ang, start_point=cir1.get_right(), end_point=cir2.get_right(), tip_length=tip)

    elif(cir1_side == "right" and cir2_side == "left"):
        return CurvedArrow(angle=ang, start_point=cir1.get_right(), end_point=cir2.get_left(), tip_length=tip)

    elif(cir1_side == "left" and cir2_side == "right"):
        return CurvedArrow(angle=ang, start_point=cir1.get_left(), end_point=cir2.get_right(), tip_length=tip)

    elif(cir1_side == "left" and cir2_side == "left"):
        return CurvedArrow(angle=ang, start_point=cir1.get_left(), end_point=cir2.get_left(), tip_length=tip)

    elif(cir1_side == "up" and cir2_side == "down"):
        return CurvedArrow(angle=ang, start_point=cir1.get_top(), end_point=cir2.get_bottom(), tip_length=tip)

    elif(cir1_side == "down" and cir2_side == "up"):
        return CurvedArrow(angle=ang, start_point=cir1.get_bottom(), end_point=cir2.get_top(), tip_length=tip)

    elif(cir1_side == "up" and cir2_side == "up"):
        return CurvedArrow(angle=ang, start_point=cir1.get_top(), end_point=cir2.get_top(), tip_length=tip)

    elif(cir1_side == "down" and cir2_side == "down"):
        return CurvedArrow(angle=ang, start_point=cir1.get_bottom(), end_point=cir2.get_bottom(), tip_length=tip)

    elif(cir1_side == "up" and cir2_side == "left"):
        return CurvedArrow(angle=ang, start_point=cir1.get_top(), end_point=cir2.get_left(), tip_length=tip)

    elif(cir1_side == "left" and cir2_side == "up"):
        return CurvedArrow(angle=ang, start_point=cir1.get_left(), end_point=cir2.get_top(), tip_length=tip)

    elif(cir1_side == "up" and cir2_side == "right"):
        return CurvedArrow(angle=ang, start_point=cir1.get_top(), end_point=cir2.get_right(), tip_length=tip)

    elif(cir1_side == "right" and cir2_side == "up"):
        return CurvedArrow(angle=ang, start_point=cir1.get_right(), end_point=cir2.get_top(), tip_length=tip)

    elif(cir1_side == "down" and cir2_side == "left"):
        return CurvedArrow(angle=ang, start_point=cir1.get_bottom(), end_point=cir2.get_left(), tip_length=tip)

    elif(cir1_side == "left" and cir2_side == "down"):
        return CurvedArrow(angle=ang, start_point=cir1.get_left(), end_point=cir2.get_bottom(), tip_length=tip)

    elif(cir1_side == "down" and cir2_side == "right"):
        return CurvedArrow(angle=ang, start_point=cir1.get_bottom(), end_point=cir2.get_right(), tip_length=tip)

    elif(cir1_side == "right" and cir2_side == "down"):
        return CurvedArrow(angle=ang, start_point=cir1.get_right(), end_point=cir2.get_bottom(), tip_length=tip)

class repeat(Scene):
    def construct(self):
        text = Text(regex_input)
        sqaures = VGroup(*[Square() for j in range(len(regex_input))]).arrange_in_grid(1, len(regex_input)).scale(0.3).shift(2 * UP)

        #States
        rep_circ1 = Circle(radius= 0.3, color= WHITE).shift(5 * LEFT)
        rep_circ2 = Circle(radius= 0.3, color= WHITE).shift(4 * LEFT)
        rep_circ3 = Circle(radius= 0.3, color= WHITE).shift(3 * LEFT)
        rep_circ4 = Circle(radius= 0.3, color= WHITE).shift(2 * LEFT)
        rep_circ5 = Circle(radius= 0.3, color= WHITE).shift(1 * LEFT)
        rep_circ6 = Circle(radius= 0.3, color= WHITE)
        rep_circ7 = Circle(radius= 0.3, color= WHITE).shift(1 * RIGHT)
        rep_acc = Circle(radius= 0.2, color= WHITE).shift(1 * RIGHT)
        rep_error = Circle(radius= 0.6, color= WHITE).shift(3 * DOWN)
        circs = [rep_circ1, rep_circ2, rep_circ3, rep_circ4, rep_circ5, rep_circ6, rep_circ7, rep_acc, rep_error]


        #State numbers
        state1 = center_text("1", rep_circ1)
        state2 = center_text("2", rep_circ2)
        state3 = center_text("3", rep_circ3)
        state4 = center_text("4", rep_circ4)
        state5 = center_text("5", rep_circ5)
        state6 = center_text("6", rep_circ6)
        state7 = center_text("7", rep_acc)
        state_error = center_text("Error", rep_error)
        states = [state1, state2, state3, state4, state5, state6, state7, state_error]


        #Arrows
        arrow_12 = drawArrows(rep_circ1, right, rep_circ2, left, 0, 0.2)
        arrow_23 = drawArrows(rep_circ2, right, rep_circ3, left, 0, 0.2)
        arrow_34 = drawArrows(rep_circ3, right, rep_circ4, left, 0, 0.2)
        arrow_45 = drawArrows(rep_circ4, right, rep_circ5, left, 0, 0.2)
        arrow_56 = drawArrows(rep_circ5, right, rep_circ6, left, 0, 0.2)
        arrow_67 = drawArrows(rep_circ6, right, rep_circ7, left, 0, 0.2)
        arrow_77 = drawArrows(rep_circ7, up, rep_circ7, right, -TAU/2, 0.2)
        arrow_19 = drawArrows(rep_circ1, down, rep_error, up, TAU/4, 0.2)
        arrow_29 = drawArrows(rep_circ2, down, rep_error, up, TAU/4, 0.2)
        arrow_39 = drawArrows(rep_circ3, down, rep_error, up, TAU/4, 0.2)
        arrow_49 = drawArrows(rep_circ4, down, rep_error, up, TAU/4, 0.2)
        arrow_59 = drawArrows(rep_circ5, down, rep_error, up, TAU/4, 0.2)
        arrow_69 = drawArrows(rep_circ6, down, rep_error, up, TAU/4, 0.2)
        arrow_99 = drawArrows(rep_error, right, rep_error, down, -TAU/2, 0.2)
        pointer = CurvedArrow(angle=0,start_point=sqaures[0].get_top() + 0.5 * UP, end_point=sqaures[0].get_top(), tip_length=0.2, color=WHITE)

        arrows = [arrow_12, arrow_23,
                  arrow_34, arrow_45,
                  arrow_56, arrow_67,
                  arrow_19, arrow_29,
                  arrow_39, arrow_49,
                  arrow_59, arrow_69,
                  arrow_77, arrow_99]
        
        _12 = Text("r", color=YELLOW).next_to(arrow_12.get_midpoint(), 0.5 * UP).scale(0.3)
        _23 = Text("e", color=YELLOW).next_to(arrow_23.get_midpoint(), 0.5 * UP).scale(0.3)      
        _34 = Text("p", color=YELLOW).next_to(arrow_34.get_midpoint(), 0.5 * UP).scale(0.3)      
        _45 = Text("e", color=YELLOW).next_to(arrow_45.get_midpoint(), 0.5 * UP).scale(0.3)
        _56 = Text("a", color=YELLOW).next_to(arrow_56.get_midpoint(), 0.5 * UP).scale(0.3)
        _67 = Text("t", color=YELLOW).next_to(arrow_67.get_midpoint(), 0.5 * UP).scale(0.3)
        _77 = Text("WS", color=YELLOW).next_to(arrow_77.get_midpoint(), 0.5 * UP).scale(0.3)
        _19 = Text("~r", color=YELLOW).next_to(arrow_19.get_midpoint(), 0.25 * LEFT).scale(0.3)
        _29 = Text("~e", color=YELLOW).next_to(arrow_29.get_midpoint(), 0.25 * LEFT).scale(0.3)
        _39 = Text("~p", color=YELLOW).next_to(arrow_39.get_midpoint(), 0.25 * LEFT).scale(0.3)
        _49 = Text("~e", color=YELLOW).next_to(arrow_49.get_midpoint(), 0.25 * LEFT).scale(0.3)
        _59 = Text("~a", color=YELLOW).next_to(arrow_59.get_midpoint(), 0.25 * LEFT).scale(0.3)
        _69 = Text("~t", color=YELLOW).next_to(arrow_69.get_midpoint(), 0.25 * LEFT).scale(0.3)
        _99 = Text("any", color=YELLOW).next_to(arrow_99.get_midpoint(), 0.25 * RIGHT).scale(0.3)

        arrows_text = [_12,_23,_34,_45, _56,_67, _77, _19,_29, _39,_49, _59,_69, _99]


        for t in range(len(text)):
            text[t].move_to(sqaures[t].get_center()).scale(0.8)

        reset_cir(circs)
        text_stack = []
        char_list = []
        count = 0
        current_state = 1
        
        self.play(AnimationGroup(*[FadeIn(s) for s in sqaures], lag_ratio=0.1), FadeIn(pointer), AnimationGroup(*[FadeIn(t) for t in text], lag_ratio=0.1))
        self.play(Create(VGroup(*circs, *states, *arrows, *arrows_text)), run_time = 9)


        def rep_12():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text_stack.append(count)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text[count].set_color(GREEN)
            reset_cir(circs)
            arrow_12.set_color(GREEN)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_circ2, GREEN, fill_opacity=1), run_time=0.5)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ2],
            *[arrow.animate for arrow in arrows],
            run_time=0.5
            )
            char_list.pop(0)

        def rep_23():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text[count].set_color(GREEN)
            text_stack.append(count)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_23.set_color(GREEN)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_circ3, GREEN, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ3],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,text[count].animate,
            run_time=0.5
            )
            char_list.pop(0)

        def rep_34():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            if(text_stack != []):
                text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text_stack.append(count)
            text[count].set_color(GREEN)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_34.set_color(GREEN)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_circ4, GREEN, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ3],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,text[count].animate,
            run_time=0.5
            )
            char_list.pop(0)

        def rep_45():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            reset_ar(arrows)
            reset_cir(circs)
            text[count].set_color(GREEN)
            text_stack.append(count)
            arrow_45.set_color(GREEN)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_circ5, GREEN, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ4],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,
            text[count].animate,
            run_time=0.5
            )
            char_list.pop(0)

        def rep_56():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text[count].set_color(GREEN)
            reset_ar(arrows)
            reset_cir(circs)
            text_stack.append(count)
            arrow_56.set_color(GREEN)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_circ6, GREEN, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ5],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,text[count].animate,
            run_time=0.5
            )
            char_list.pop(0)

        def rep_67():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text[count].set_color(GREEN)
            text_stack.append(count)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_67.set_color(GREEN)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_circ7, GREEN, fill_opacity=1), run_time=1),
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ6],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,text[count].animate,
            run_time=0.5
            )
            char_list.pop(0)

        def rep_77():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            if not bool(re.search(whitespace, regex_input[text_stack[len(text_stack) - 1]])) :
                text[text_stack[len(text_stack) - 1]].set_color(WHITE)
                self.play(text[text_stack[len(text_stack) - 1]].animate)
            # text[count].set_color(GREEN)
            text_stack.append(count)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_77.set_color(GREEN)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_circ7, GREEN, fill_opacity=1), run_time=1),
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ7],
            *[arrow.animate for arrow in arrows],
            run_time=0.5
            )

            char_list.pop(0)

        def rep_1E():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text_stack.append(count)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text[count].set_color(GREEN).scale(1.2)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_19.set_color(PURE_RED)
            char_list.pop(0)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_error, PURE_RED, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ1],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,
            text[count].animate, run_time=0.5
            )

        def rep_2E():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text_stack.append(count)
            text[count].set_color(GREEN).scale(1.2)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_29.set_color(PURE_RED)
            char_list.pop(0)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_error, PURE_RED, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ2],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,
            text[count].animate, run_time=0.5
            )

        def rep_3E():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text_stack.append(count)
            text[count].set_color(GREEN).scale(1.2)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_39.set_color(PURE_RED)
            char_list.pop(0)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_error, PURE_RED, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ3],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,
            text[count].animate, run_time=0.5
            )

        def rep_4E():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text_stack.append(count)
            text[count].set_color(GREEN).scale(1.2)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_49.set_color(PURE_RED)
            char_list.pop(0)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_error, PURE_RED, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ4],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,
            text[count].animate, run_time=0.5
            )

        def rep_5E():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text_stack.append(count)
            text[count].set_color(GREEN).scale(1.2)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_59.set_color(PURE_RED)
            char_list.pop(0)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_error, PURE_RED, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ5],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,
            text[count].animate, run_time=0.5
            )

        def rep_6E():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text_stack.append(count)
            text[count].set_color(GREEN).scale(1.2)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_69.set_color(PURE_RED)
            char_list.pop(0)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_error, PURE_RED, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ6],
            *[arrow.animate for arrow in arrows],
            text[text_stack[len(text_stack) - 1]].animate,
            text[count].animate, run_time=0.5
            )

        def rep_EE():
            pointer.move_to(sqaures[count].get_top()+ 0.5 * UP)
            # text[text_stack[len(text_stack) - 1]].set_color(WHITE)
            text_stack.append(count)
            # if regex_input[count] != ' ':
            #     text[count].set_color(GREEN).scale(1.2)
            reset_ar(arrows)
            reset_cir(circs)
            arrow_99.set_color(PURE_RED)
            char_list.pop(0)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(rep_error, PURE_RED, fill_opacity=1), run_time=1)
            self.play(
            *[circle.animate for circle in circs if circle != rep_circ6],
            *[arrow.animate for arrow in arrows],
            # text[text_stack[len(text_stack) - 1]].animate,
            run_time=0.5
            )

        
        for c in regex_input:
            char_list.append(c)
        current_state = 1

        # Logic of the DFA
        while(len(char_list)):
            if current_state == 1:
                if char_list[0] == 'r':
                    rep_12()                    
                    current_state = 2
                    count = count + 1
                else:
                    rep_1E()                    
                    current_state = 9
                    count = count + 1
            elif current_state == 2:
                if char_list[0] == 'e':
                    rep_23()
                    current_state = 3
                    count = count + 1
                else:
                    rep_2E()                    
                    current_state = 9
                    count = count + 1
            elif current_state == 3:
                if char_list[0] == 'p':
                    rep_34()
                    current_state = 4
                    count = count + 1
                else:
                    rep_3E()                    
                    current_state = 9
                    count = count + 1
            elif current_state == 4:
                if char_list[0] == 'e':
                    rep_45()
                    current_state = 5
                    count = count + 1
                else:
                    rep_4E()                    
                    current_state = 9
                    count = count + 1

            elif current_state == 5:
                if char_list[0] == 'a':
                    rep_56()
                    current_state = 6
                    count = count + 1
                else:
                    rep_5E()                    
                    current_state = 9
                    count = count + 1
            elif current_state == 6:
                if char_list[0] == 't':
                    rep_67()
                    current_state = 7
                    count = count + 1
                else:
                    rep_6E()                    
                    current_state = 9
                    count = count + 1
            elif current_state == 7:
                if  bool(re.search(whitespace, char_list[0])):
                    rep_77()
                    current_state = 7
                    count = count + 1
                else:
                    current_state = 9
                    count = count + 1
            elif current_state == 9:
                rep_EE()
                current_state = 9
                count = count + 1


class ID(Scene):
    def construct(self):

        #circles
        id_circ1 = Circle(radius= 0.3, color= WHITE).shift(2 * LEFT)
        id_circ2 = Circle(radius= 0.3, color= WHITE).shift(2 * RIGHT)
        id_circ3 = Circle(radius= 0.3, color= WHITE).shift(2 * DOWN)
        circs = [id_circ1, id_circ2, id_circ3]

        #State numbers
        state1 = center_text("1", id_circ1)
        state2 = center_text("2", id_circ2)
        state3 = center_text("3", id_circ3)
        states = [state1, state2, state3]

        #Arrows
        arrow_12 = drawArrows(id_circ1, right, id_circ2, left, 0, 0.2)
        arrow_13 = drawArrows(id_circ1, down, id_circ3, up, 0, 0.2)
        arrow_22 = drawArrows(id_circ2, up, id_circ2, right, -TAU/2, 0.2)
        arrow_23 = drawArrows(id_circ2, down, id_circ3, up, 0, 0.2)
        arrow_33 = drawArrows(id_circ3, right, id_circ3, down, -TAU/2, 0.2)
        
        arrows = [arrow_12, arrow_13, arrow_22, arrow_23, arrow_33]

        _12 = Text("letter", color=YELLOW).next_to(arrow_12.get_midpoint(), 0.5 * UP).scale(0.3)
        _13 = Text("~letter", color=YELLOW).next_to(arrow_13.get_midpoint(), 0.5 * LEFT).scale(0.3)      
        _22 = Text("letter, NUM", color=YELLOW).next_to(arrow_22.get_midpoint(), 0.5 * UP).scale(0.3)      
        _23 = Text("~letter, ~NUM", color=YELLOW).move_to(arrow_23.get_right() + 0.2 * RIGHT).scale(0.3)
        _33 = Text("any", color=YELLOW).next_to(arrow_33.get_midpoint(), 0.5 * DOWN).scale(0.3)

        arrows_text = [_12, _13, _22, _23, _33]

        self.play(Create(VGroup(*circs, *states, *arrows, *arrows_text)), run_time = 9)

class until(Scene):
    def construct(self):

        #circles
        unt_circ1 = Circle(radius= 0.3, color= WHITE).shift(5 * LEFT)
        unt_circ2 = Circle(radius= 0.3, color= WHITE).shift(4 * LEFT)
        unt_circ3 = Circle(radius= 0.3, color= WHITE).shift(3 * LEFT)
        unt_circ4 = Circle(radius= 0.3, color= WHITE).shift(2 * LEFT)
        unt_circ5 = Circle(radius= 0.3, color= WHITE).shift(1 * LEFT)
        unt_circ6 = Circle(radius= 0.3, color= WHITE)
        unt_circ7 = Circle(radius= 0.3, color= WHITE).shift(1 * RIGHT)
        unt_circ8 = Circle(radius= 0.3, color= WHITE).shift(2 * RIGHT)
        unt_circE = Circle(radius= 0.8, color= WHITE).shift(2 * DOWN).shift(2 * LEFT)
        circs = [unt_circ1, unt_circ2, unt_circ3, unt_circ4, unt_circ5, unt_circ6, unt_circ7, unt_circ8, unt_circE]

        #State numbers
        state1 = center_text("1",     unt_circ1)
        state2 = center_text("2",     unt_circ2)
        state3 = center_text("3",     unt_circ3)
        state4 = center_text("4",     unt_circ4)
        state5 = center_text("5",     unt_circ5)
        state6 = center_text("6",     unt_circ6)
        state7 = center_text("ID",    unt_circ7)
        state8 = center_text("8",     unt_circ8)
        stateE = center_text("ERROR", unt_circE)
        states = [state1, state2, state3, state4, state5, state6, state7, state8, stateE]

        #Arrows
        arrow_12 = drawArrows(unt_circ1, right, unt_circ2, left, 0, 0.2)
        arrow_23 = drawArrows(unt_circ2, right, unt_circ3, left, 0, 0.2)
        arrow_34 = drawArrows(unt_circ3, right, unt_circ4, left, 0, 0.2)
        arrow_45 = drawArrows(unt_circ4, right, unt_circ5, left, 0, 0.2)
        arrow_56 = drawArrows(unt_circ5, right, unt_circ6, left, 0, 0.2)
        arrow_67 = drawArrows(unt_circ6, right, unt_circ7, left, 0, 0.2)
        arrow_78 = drawArrows(unt_circ7, right, unt_circ8, left, 0, 0.2)
        arrow_88 = drawArrows(unt_circ8, right, unt_circ8, down, -TAU/2, 0.2)
        arrow_1E = drawArrows(unt_circ1, down, unt_circE, left, TAU/4 , 0.2)
        arrow_2E = drawArrows(unt_circ2, down, unt_circE, left, TAU/4 , 0.2)
        arrow_3E = drawArrows(unt_circ3, down, unt_circE, left, TAU/4 , 0.2)
        arrow_4E = drawArrows(unt_circ4, down, unt_circE, up, 0, 0.2)
        arrow_5E = drawArrows(unt_circ5, down, unt_circE, right, -TAU/4 , 0.2)
        arrow_6E = drawArrows(unt_circ6, down, unt_circE, right, -TAU/4 , 0.2)
        arrow_7E = drawArrows(unt_circ7, down, unt_circE, right, -TAU/4 , 0.2)
        
        arrows = [arrow_12, arrow_23,
                  arrow_34, arrow_45,
                  arrow_56, arrow_67,
                  arrow_78, arrow_88,
                  arrow_1E, arrow_5E,
                  arrow_2E, arrow_6E,
                  arrow_3E, arrow_7E,
                  arrow_4E,]


        _12 = Text("u", color=YELLOW).move_to(     arrow_12.get_midpoint() + 0.3 * UP).scale(0.3)
        _23 = Text("n", color=YELLOW).move_to(     arrow_23.get_midpoint() + 0.3 * UP).scale(0.3)
        _34 = Text("t", color=YELLOW).move_to(     arrow_34.get_midpoint() + 0.3 * UP).scale(0.3)
        _45 = Text("i", color=YELLOW).move_to(     arrow_45.get_midpoint() + 0.3 * UP).scale(0.3)
        _56 = Text("l", color=YELLOW).move_to(     arrow_56.get_midpoint() + 0.3 * UP).scale(0.3)
        _67 = Text("space", color=YELLOW).move_to( arrow_67.get_midpoint() + 0.3 * UP).scale(0.2)
        _78 = Text("=", color=YELLOW).move_to(     arrow_78.get_midpoint() + 0.3 * UP).scale(0.3)
        _88 = Text("NUM", color=YELLOW).move_to(   arrow_88.get_midpoint() + 0.5 * DOWN).scale(0.3)
        _1E = Text("~u", color=YELLOW).move_to(    arrow_1E.get_midpoint() + 0.7 * LEFT).scale(0.3)
        _2E = Text("~n", color=YELLOW).move_to(    arrow_2E.get_midpoint() + 0.4 * LEFT).scale(0.3)
        _3E = Text("~t", color=YELLOW).move_to(    arrow_3E.get_midpoint() + 0.3 * LEFT).scale(0.3)
        _4E = Text("~i", color=YELLOW).move_to(    arrow_4E.get_midpoint() + 0.3 * LEFT).scale(0.3)
        _5E = Text("~l", color=YELLOW).move_to(    arrow_5E.get_midpoint() + 0.3 * LEFT).scale(0.3)
        _6E = Text("~space", color=YELLOW).move_to(arrow_6E.get_midpoint() + 0.3 * LEFT).scale(0.2)
        _7E = Text("~=", color=YELLOW).move_to(    arrow_7E.get_midpoint() + 0.3 * LEFT).scale(0.3)

        arrows_text = [_12, _23, _34, _45, _56, _67, _78, _88, _1E, _2E, _3E, _4E, _5E, _6E, _7E]

        self.play(Create(VGroup(*circs, *states, *arrows, *arrows_text)), run_time = 9)

class loop(Scene):
    def construct(self):
        
        #circles
        loop_circ1 = Circle(radius= 0.7, color= WHITE).shift(3 * LEFT)
        loop_circ2 = Circle(radius= 0.3, color= WHITE)
        loop_circ3 = Circle(radius= 0.3, color= WHITE).shift(2 * RIGHT)
        loop_circ4 = Circle(radius= 0.7, color= WHITE).shift(4.2 * RIGHT)
        loop_circ5 = Circle(radius= 0.7, color= WHITE).shift(2.5 * DOWN)
        circs = [loop_circ1, loop_circ2, loop_circ3, loop_circ4, loop_circ5]

        #State numbers
        state1 = center_text("repeat", loop_circ1)
        state2 = center_text("2", loop_circ2)
        state3 = center_text("3", loop_circ3)
        state4 = center_text("until", loop_circ4)
        state5 = center_text("error", loop_circ5)
        states = [state1, state2, state3, state4, state5]

        #Arrows
        arrow_R2 = drawArrows(loop_circ1, right, loop_circ2, left, 0, 0.2)
        arrow_22 = drawArrows(loop_circ2, left, loop_circ2, up, -TAU/2, 0.2)
        arrow_23 = drawArrows(loop_circ2, right, loop_circ3, left, 0, 0.2)
        arrow_32 = drawArrows(loop_circ3, up, loop_circ2, up, TAU/4, 0.2)
        arrow_3U = drawArrows(loop_circ3, right, loop_circ4, left, 0, 0.2)
        arrow_2E = drawArrows(loop_circ2, down, loop_circ5, up, 0, 0.2)
        arrow_RE = drawArrows(loop_circ1, down, loop_circ5, left, TAU/4, 0.2)
        
        arrows = [arrow_R2, arrow_22, arrow_22, arrow_23, arrow_32, arrow_3U, arrow_2E, arrow_RE]

        _R2 = Text("letter", color=YELLOW).next_to(arrow_R2.get_midpoint(), 0.3 * UP).scale(0.3)
        _22 = Text("letter, NUM", color=YELLOW).next_to(arrow_22.get_midpoint(), 0.3 * UP).scale(0.3)      
        _23 = Text(";", color=YELLOW).next_to(arrow_23.get_midpoint(), 0.3 * UP).scale(0.3)      
        _32 = Text("letter", color=YELLOW).move_to(arrow_32.get_midpoint() + 0.2 * UP).scale(0.3)
        _3U = Text("U", color=YELLOW).next_to(arrow_3U.get_midpoint(), 0.5 * DOWN).scale(0.3)
        _2E = Text("~letter, ~NUM", color=YELLOW).move_to(arrow_2E.get_midpoint()).scale(0.3).shift(0.7 * RIGHT)
        _RE = Text("~letter", color=YELLOW).next_to(arrow_RE.get_midpoint(), 0.5 * DOWN).scale(0.3)

        arrows_text = [_R2, _32, _22, _23, _3U, _2E, _RE]

        self.play(Create(VGroup(*circs, *states, *arrows, *arrows_text)), run_time = 9)
