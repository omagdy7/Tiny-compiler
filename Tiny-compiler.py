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

def reset_txt(txt):
    for ch in txt:
        ch.set_color(WHITE)

# Function that centers text in the middle of a circle
def center_text(txt, circ):
    return Text(txt).move_to(circ.get_center()).scale(0.4)

def shiftcirc(circ, up, right, down, left):
    pass
    

# Function that draws arrows between circs based on input
def drawArrows(cir1, cir1_side, cir2, cir2_side, ang, tip=0.2):
    if cir1_side == "right" and cir2_side == "right" :
        return CurvedArrow(angle=ang, start_point=cir1.get_right(), end_point=cir2.get_right(), tip_length=tip)

    elif cir1_side == "right" and cir2_side == "left" :
        return CurvedArrow(angle=ang, start_point=cir1.get_right(), end_point=cir2.get_left(), tip_length=tip)

    elif cir1_side == "left" and cir2_side == "right" :
        return CurvedArrow(angle=ang, start_point=cir1.get_left(), end_point=cir2.get_right(), tip_length=tip)

    elif cir1_side == "left" and cir2_side == "left" :
        return CurvedArrow(angle=ang, start_point=cir1.get_left(), end_point=cir2.get_left(), tip_length=tip)

    elif cir1_side == "up" and cir2_side == "down" :
        return CurvedArrow(angle=ang, start_point=cir1.get_top(), end_point=cir2.get_bottom(), tip_length=tip)

    elif cir1_side == "down" and cir2_side == "up" :
        return CurvedArrow(angle=ang, start_point=cir1.get_bottom(), end_point=cir2.get_top(), tip_length=tip)

    elif cir1_side == "up" and cir2_side == "up" :
        return CurvedArrow(angle=ang, start_point=cir1.get_top(), end_point=cir2.get_top(), tip_length=tip)

    elif cir1_side == "down" and cir2_side == "down" :
        return CurvedArrow(angle=ang, start_point=cir1.get_bottom(), end_point=cir2.get_bottom(), tip_length=tip)

    elif cir1_side == "up" and cir2_side == "left" :
        return CurvedArrow(angle=ang, start_point=cir1.get_top(), end_point=cir2.get_left(), tip_length=tip)

    elif cir1_side == "left" and cir2_side == "up" :
        return CurvedArrow(angle=ang, start_point=cir1.get_left(), end_point=cir2.get_top(), tip_length=tip)

    elif cir1_side == "up" and cir2_side == "right" :
        return CurvedArrow(angle=ang, start_point=cir1.get_top(), end_point=cir2.get_right(), tip_length=tip)

    elif cir1_side == "right" and cir2_side == "up" :
        return CurvedArrow(angle=ang, start_point=cir1.get_right(), end_point=cir2.get_top(), tip_length=tip)

    elif cir1_side == "down" and cir2_side == "left" :
        return CurvedArrow(angle=ang, start_point=cir1.get_bottom(), end_point=cir2.get_left(), tip_length=tip)

    elif cir1_side == "left" and cir2_side == "down" :
        return CurvedArrow(angle=ang, start_point=cir1.get_left(), end_point=cir2.get_bottom(), tip_length=tip)

    elif cir1_side == "down" and cir2_side == "right" :
        return CurvedArrow(angle=ang, start_point=cir1.get_bottom(), end_point=cir2.get_right(), tip_length=tip)

    elif cir1_side == "right" and cir2_side == "down" :
        return CurvedArrow(angle=ang, start_point=cir1.get_right(), end_point=cir2.get_bottom(), tip_length=tip)

class repeat(MovingCameraScene, Scene):
    def construct(self):
        text = Text(regex_input)
        squares = VGroup(*[Square() for j in range(len(regex_input))]).arrange_in_grid(1, len(regex_input)).scale(0.3).shift(2 * UP)
        text_stack = []
        char_list = []
        count = 0
        current_state = 1

        #repeat states
        circ1  = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 5 * LEFT)
        circ2  = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 4 * LEFT)
        circ3  = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 3 * LEFT)
        circ4  = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 2 * LEFT)
        circ5  = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 1 * LEFT)
        circ6  = Circle(radius= 0.2, color= WHITE).shift(3 * UP)
        circ7  = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 1 * RIGHT)
        circ8  = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 2 * RIGHT)
        circ9  = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 3 * RIGHT)
        circ10 = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 4 * RIGHT)
        circ11 = Circle(radius= 0.2, color= WHITE).shift(3 * UP, 4.7 * RIGHT)
        circ12 = Circle(radius= 0.2, color= WHITE).shift(4.7 * RIGHT, 2.1 * UP)
        circ13 = Circle(radius= 0.2, color= WHITE).shift(4.7 * RIGHT, 2 * UP)
        circ13 = Circle(radius= 0.2, color= WHITE).shift(4.7 * RIGHT, 1 * UP)
        circ14 = Circle(radius= 0.2, color= WHITE).shift(4.7 * RIGHT)
        circ15 = Circle(radius= 0.2, color= WHITE).shift(4.7 * RIGHT, 1 * DOWN)
        circ16 = Circle(radius= 0.2, color= WHITE).shift(4.7 * RIGHT, 2 * DOWN)
        circ17 = Circle(radius= 0.2, color= WHITE).shift(4.7 * RIGHT, 3 * DOWN)
        circ18 = Circle(radius= 0.2, color= WHITE).shift(3 * DOWN, 4 * RIGHT)
        circ19 = Circle(radius= 0.2, color= WHITE).shift(3 * DOWN, 3 * RIGHT)
        circ20 = Circle(radius= 0.2, color= WHITE).shift(3 * DOWN, 2 * RIGHT)
        circ21 = Circle(radius= 0.2, color= WHITE).shift(3 * DOWN, 1 * RIGHT)
        circ22 = Circle(radius= 0.2, color= WHITE).shift(3 * DOWN)
        circ23 = Circle(radius= 0.2, color= WHITE).shift(3 * DOWN, 1 * LEFT)
        circ24 = Circle(radius= 0.2, color= WHITE).shift(3 * DOWN, 2 * LEFT)
        circ25 = Circle(radius= 0.2, color= WHITE).shift(3 * DOWN, 3 * LEFT)
        dfa_error   = Circle(radius= 0.7, color= WHITE).shift(4 * LEFT)

        circs = [circ1,  circ2 , circ3,
                 circ4 , circ5,  circ6 ,
                 circ7,  circ8 , circ9,
                 circ10, circ11, circ12,
                 circ13, circ13, circ14,
                 circ15, circ16, circ17,
                 circ18, circ19, circ20,
                 circ21, circ22, circ23,
                 circ24, circ25]


        #repeat state numbers
        state1  = center_text("1",        circ1)
        state2  = center_text("2",        circ2)
        state3  = center_text("3",        circ3)
        state4  = center_text("4",        circ4)
        state5  = center_text("5",        circ5)
        state6  = center_text("6",        circ6)
        state7  = center_text("7",        circ7)
        state8  = center_text("8",        circ8)
        state9  = center_text("9",        circ9)
        state10 = center_text("10",       circ10)
        state11 = center_text("11",       circ11)
        state12 = center_text("12",       circ12)
        state13 = center_text("13",       circ13)
        state14 = center_text("14",       circ14)
        state15 = center_text("15",       circ15)
        state16 = center_text("16",       circ16)
        state17 = center_text("17",       circ17)
        state18 = center_text("18" ,      circ18)
        state19 = center_text("19" ,      circ19)
        state20 = center_text("20" ,      circ20)
        state21 = center_text("21" ,      circ21)
        state22 = center_text("22",       circ22)
        state23 = center_text("23",       circ23)
        state24 = center_text("24",       circ24)
        state25 = center_text("25",       circ25)
        state26 = center_text("26",       dfa_error)

        states = [state1, state2,
                  state3, state4,
                  state5, state6,
                  state7, state8,
                  state9, state10,
                  state11, state12,
                  state13, state14,
                  state15, state16,
                  state17, state18,
                  state19, state20,
                  state21, state22,
                  state23, state24,
                  state25, state26]



        #repeat arrows
        arrow_12 = drawArrows(circ1, right,       circ2,     left,   0)
        arrow_23 = drawArrows(circ2, right,       circ3,     left,   0)
        arrow_34 = drawArrows(circ3, right,       circ4,     left,   0)
        arrow_45 = drawArrows(circ4, right,       circ5,     left,   0)
        arrow_56 = drawArrows(circ5, right,       circ6,     left,   0)
        arrow_67 = drawArrows(circ6, right,       circ7,     left,   0)
        arrow_78 = drawArrows(circ7, up,          circ7,     right, -TAU/2)
        arrow_89 = drawArrows(circ1, down,        circ8,     up,     TAU/4)
        arrow_99 = drawArrows(circ2, down,        circ8,     up,     TAU/4)
        arrow_39 = drawArrows(circ3, down,        circ8,     up,     TAU/4)
        arrow_49 = drawArrows(circ4, down,        circ8,     up,     TAU/4)
        arrow_59 = drawArrows(circ5, down,        circ8,     up,     TAU/4)
        arrow_69 = drawArrows(circ6, down,        circ8,     up,     TAU/4)
        arrow_99 = drawArrows(dfa_error, right,   circ8,     down,   -TAU/2)
        arrow_9A = drawArrows(circ1, right,       circ2,     left,   0)
        arrow_AB = drawArrows(circ2, right,       circ3,     left,   0)
        arrow_BC = drawArrows(circ3, right,       circ4,     left,   0)
        arrow_CD = drawArrows(circ4, right,       circ5,     left,   0)
        arrow_DE = drawArrows(circ5, right,       circ6,     left,   0)
        arrow_EF = drawArrows(circ6, right,       circ7,     left,   0)
        arrow_GA = drawArrows(circ7, right,       circ8,     left,   0)
        arrow_9A = drawArrows(circ8, right,       circ8,     down,   -TAU/2)
        arrow_9A = drawArrows(circ1, down,        circ1,     left,   TAU/4 )
        arrow_9A = drawArrows(circ2, down,        circ1,     left,   TAU/4 )
        arrow_9A = drawArrows(circ3, down,        circ1,     left,   TAU/4 )
        arrow_9A = drawArrows(circ4, down,        circ1,     up,     0     )
        arrow_9A = drawArrows(circ5, down,        circ1,     right,  -TAU/4)
        arrow_9A = drawArrows(circ6, down,        circ1,     right,  -TAU/4)
        arrow_9A = drawArrows(circ7, down,        circ1,     right,  -TAU/4)
        arrow_9A = drawArrows(circ1, right,       circ2,     left,   0     )
        arrow_9A = drawArrows(circ2, left,        circ2,     up,     -TAU/2)
        arrow_9A = drawArrows(circ2, right,       circ3,     left,   0    )
        arrow_9A = drawArrows(circ3, up,          circ2,     right,  TAU/4)
        arrow_9A = drawArrows(circ3, down,        circ4,     up,     0    )
        arrow_9A = drawArrows(circ2, down,        dfa_error, left,   TAU/4)
        arrow_9A = drawArrows(circ1, down,        dfa_error, left,   TAU/4)
        arrow_9A = drawArrows(circ3, down,        dfa_error, left,   TAU/4)
        arrow_9A = drawArrows(circ5, down,        dfa_error, left,   TAU/4)
        arrow_9A = drawArrows(circ6, down,        dfa_error, left,   TAU/4)
        arrow_9A = drawArrows(circ7, down,        dfa_error, left,   TAU/4)
        
        pointer = CurvedArrow(angle=0,start_point=squares[0].get_top() + 0.5 * UP, end_point=squares[0].get_top(), tip_length=0.2, color=WHITE)

        arrows = [arrow_12, arrow_23,
                  arrow_34, arrow_45,
                  arrow_56, arrow_67,
                  arrow_19, arrow_29,
                  arrow_39, arrow_49,
                  arrow_59, arrow_69,
                  arrow_77, arrow_99]
        
        rep_txt_12 = Text("r", color=YELLOW).next_to(arrow_12.get_midpoint(), 0.5 * UP).scale(0.3)
        rep_txt_23 = Text("e", color=YELLOW).next_to(arrow_23.get_midpoint(), 0.5 * UP).scale(0.3)      
        rep_txt_34 = Text("p", color=YELLOW).next_to(arrow_34.get_midpoint(), 0.5 * UP).scale(0.3)      
        rep_txt_45 = Text("e", color=YELLOW).next_to(arrow_45.get_midpoint(), 0.5 * UP).scale(0.3)
        rep_txt_56 = Text("a", color=YELLOW).next_to(arrow_56.get_midpoint(), 0.5 * UP).scale(0.3)
        rep_txt_67 = Text("t", color=YELLOW).next_to(arrow_67.get_midpoint(), 0.5 * UP).scale(0.3)
        rep_txt_77 = Text("WS", color=YELLOW).next_to(arrow_77.get_midpoint(), 0.5 * UP).scale(0.3)
        rep_txt_19 = Text("~r", color=YELLOW).next_to(arrow_19.get_midpoint(), 0.25 * LEFT).scale(0.3)
        rep_txt_29 = Text("~e", color=YELLOW).next_to(arrow_29.get_midpoint(), 0.25 * LEFT).scale(0.3)
        rep_txt_39 = Text("~p", color=YELLOW).next_to(arrow_39.get_midpoint(), 0.25 * LEFT).scale(0.3)
        rep_txt_49 = Text("~e", color=YELLOW).next_to(arrow_49.get_midpoint(), 0.25 * LEFT).scale(0.3)
        rep_txt_59 = Text("~a", color=YELLOW).next_to(arrow_59.get_midpoint(), 0.25 * LEFT).scale(0.3)
        rep_txt_69 = Text("~t", color=YELLOW).next_to(arrow_69.get_midpoint(), 0.25 * LEFT).scale(0.3)
        rep_txt_99 = Text("any", color=YELLOW).next_to(arrow_99.get_midpoint(), 0.25 * RIGHT).scale(0.3)
        unt_txt_12 = Text("u", color=YELLOW).move_to(     unt_arrow_12.get_midpoint() + 0.3 * UP).scale(0.3)
        unt_txt_23 = Text("n", color=YELLOW).move_to(     unt_arrow_23.get_midpoint() + 0.3 * UP).scale(0.3)
        unt_txt_34 = Text("t", color=YELLOW).move_to(     unt_arrow_34.get_midpoint() + 0.3 * UP).scale(0.3)
        unt_txt_45 = Text("i", color=YELLOW).move_to(     unt_arrow_45.get_midpoint() + 0.3 * UP).scale(0.3)
        unt_txt_56 = Text("l", color=YELLOW).move_to(     unt_arrow_56.get_midpoint() + 0.3 * UP).scale(0.3)
        unt_txt_67 = Text("space", color=YELLOW).move_to( unt_arrow_67.get_midpoint() + 0.3 * UP).scale(0.2)
        unt_txt_78 = Text("=", color=YELLOW).move_to(     unt_arrow_78.get_midpoint() + 0.3 * UP).scale(0.3)
        unt_txt_88 = Text("NUM", color=YELLOW).move_to(   unt_arrow_88.get_midpoint() + 0.5 * DOWN).scale(0.3)
        unt_txt_1E = Text("~u", color=YELLOW).move_to(    unt_arrow_1E.get_midpoint() + 0.7 * LEFT).scale(0.3)
        unt_txt_2E = Text("~n", color=YELLOW).move_to(    unt_arrow_2E.get_midpoint() + 0.4 * LEFT).scale(0.3)
        unt_txt_3E = Text("~t", color=YELLOW).move_to(    unt_arrow_3E.get_midpoint() + 0.3 * LEFT).scale(0.3)
        unt_txt_4E = Text("~i", color=YELLOW).move_to(    unt_arrow_4E.get_midpoint() + 0.3 * LEFT).scale(0.3)
        unt_txt_5E = Text("~l", color=YELLOW).move_to(    unt_arrow_5E.get_midpoint() + 0.3 * LEFT).scale(0.3)
        unt_txt_6E = Text("~space", color=YELLOW).move_to(unt_arrow_6E.get_midpoint() + 0.3 * LEFT).scale(0.2)
        unt_txt_7E = Text("~=", color=YELLOW).move_to(    unt_arrow_7E.get_midpoint() + 0.3 * LEFT).scale(0.3)
        loop_text_R2 = Text("letter", color=YELLOW).next_to(loop_arrow_R2.get_midpoint(), 0.3 * UP).scale(0.3)
        loop_text_22 = Text("letter, NUM", color=YELLOW).next_to(loop_arrow_22.get_midpoint(), 0.3 * UP).scale(0.3)      
        loop_text_23 = Text(";", color=YELLOW).next_to(loop_arrow_23.get_midpoint(), 0.3 * UP).scale(0.3)      
        loop_text_32 = Text("letter", color=YELLOW).move_to(loop_arrow_32.get_midpoint() + 0.2 * UP).scale(0.3)
        loop_text_3U = Text("U", color=YELLOW).next_to(loop_arrow_3U.get_midpoint(), 0.5 * DOWN).scale(0.3)
        loop_text_2E = Text("~letter, ~NUM", color=YELLOW).move_to(loop_arrow_2E.get_midpoint()).scale(0.3).shift(0.7 * RIGHT)
        loop_text_RE = Text("~letter", color=YELLOW).next_to(loop_arrow_RE.get_midpoint(), 0.5 * DOWN).scale(0.3)

        for t in range(len(text)):
            text[t].move_to(squares[t].get_center()).scale(0.8)

        reset_cir(circs)
        # self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.1), FadeIn(pointer), AnimationGroup(*[FadeIn(t) for t in text], lag_ratio=0.1))
        # self.play(Create(VGroup(*circs, *states, *arrows, *arrows_text)), run_time = 9)
        self.play(Create(VGroup(*circs, *states), run_time=4))
        # self.play(Create(VGroup(*unt_circs, *unt_states, *unt_arrows, *unt_arrows_text)), run_time = 9)
        # self.play(Create(VGroup(*loop_circs, *loop_states, *loop_arrows, *loop_arrows_text)), run_time = 2)
        # self.camera.frame.save_state()
        # self.play(self.camera.frame.animate.set(width=loop_circ4.width * 2).move_to(loop_circ4))
        # self.play(FadeOut(VGroup(*loop_circs, *loop_states, *loop_arrows, *loop_arrows_text)), run_time = 0.1)
        # self.play(FadeIn(VGroup(*circs, *states, *arrows, *arrows_text).shift(1.5 * UR)), run_time = 0.0001)
        # self.play(Restore(self.camera.frame))
        # self.wait(0.3)

        def play_animation(squares, circs, arrows, pointer, arrow ,circ_reset):
            pointer.move_to(squares[count].get_top()+ 0.5 * UP)
            text_stack.append(count)
            if regex_input[count].isalpha():
                text[count].set_color(GREEN)
            reset_cir(circs)
            reset_ar(arrows)
            arrow.set_color(GREEN)
            self.play(FadeIn(pointer))
            self.play(FadeToColor(circ_reset, GREEN, fill_opacity=1), run_time=0.5)
            self.play(
            *[circle.animate for circle in circs if circle != circ_reset],
            *[arrow.animate for arrow in arrows],
            run_time=0.5
            )
            reset_txt(text)
            self.play(*[ch.animate for ch in text], run_time=0.0001)
            char_list.pop(0)


        
        for c in regex_input:
            char_list.append(c)
        current_state = 1



        #Logic of repeat DFA
        while(len(char_list)):
            c = char_list[0]
            error = 25
            match current_state:
                case 1:
                    if c == 'r':
                        play_animation(squares, circs, arrows, pointer, arrow_12, rep_circ2)
                        current_state = 2
                        count = count + 1
                    else:
                        play_animation(squares, circs, arrows, pointer, arrow_19, dfa_error)
                        current_state = error
                        count = count + 1
                case 2:
                    if c == 'e':
                        play_animation(squares, circs, arrows, pointer, arrow_23, rep_circ3)
                        current_state = 3
                        count = count + 1
                    else:
                        play_animation(squares, circs, arrows, pointer, arrow_29, dfa_error)
                        current_state = error
                        count = count + 1
                case 3:
                    if c == 'p':
                        play_animation(squares, circs, arrows, pointer, arrow_34, rep_circ4)
                        current_state = 4
                        count = count + 1
                    else:
                        play_animation(squares, circs, arrows, pointer, arrow_39, dfa_error)
                        current_state = error
                        count = count + 1
                case 4:
                    if c == 'e':
                        play_animation(squares, circs, arrows, pointer, arrow_45, rep_circ5)
                        current_state = 5
                        count = count + 1
                    else:
                        play_animation(squares, circs, arrows, pointer, arrow_49, dfa_error)
                        current_state = error
                        count = count + 1
                case 5:
                    if c == 'a':
                        play_animation(squares, circs, arrows, pointer, arrow_56, rep_circ6)
                        current_state = 6
                        count = count + 1
                    else:
                        play_animation(squares, circs, arrows, pointer, arrow_59, dfa_error)
                        current_state = error
                        count = count + 1
                case 6:
                    if c == 't':
                        play_animation(squares, circs, arrows, pointer, arrow_67, rep_circ7)
                        current_state = 7
                        count = count + 1
                    else:
                        play_animation(squares, circs, arrows, pointer, arrow_67, dfa_error)
                        current_state = error
                        count = count + 1
                case 7:
                    if  bool(re.search(whitespace, c)):
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 7
                        count = count + 1
                    elif c.isalpha():
                        play_animation(squares, circs, arrows, pointer, loop_arrow_R2, loop_circ2)
                        current_state = 8
                        count = count + 1
                    else:
                        play_animation(squares, circs, arrows, pointer, loop_arrow_RE, dfa_error)
                        current_state = error
                        count = count + 1
                case 8:
                    if  c == ' ':
                        play_animation(squares, circs, arrows, pointer, loop_arrow_RE, dfa_error)
                        current_state = 9
                        count = count + 1
                    elif c.isalnum():
                        current_state = 8
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1

                case 9:
                    if  c == ':':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 10:
                    if  c == '=':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 11:
                    if  c == ' ':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 12:
                    if  c == ';':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 13:
                    if  c == ':':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 14:
                    if  c == 'U' or 'u':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 15:
                    if  c == 'n':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 16:
                    if  c == 't':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 17:
                    if  c == 'i':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 18:
                    if  c == 'l':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 19:
                    if  c == ' ':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 20:
                    if  c.isalpha():
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 21:
                    if  c == ' ':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 22:
                    if  c == ' ':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 23:
                    if  c == ' ':
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case 24:
                    if  c.isnumeric():
                        play_animation(squares, circs, arrows, pointer, arrow_77, rep_circ7)
                        current_state = 10
                        count = count + 1
                    else:
                        current_state = error
                        count = count + 1
                case error:
                    current_state = error
                    count = count + 1
