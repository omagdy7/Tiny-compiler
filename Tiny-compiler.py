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
    return Text(txt).move_to(circ.get_center()).scale(0.6)

# Function that draws arrows between circs based on input
def drawArrows(cir1, cir1_side, cir2, cir2_side, ang, tip):
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
        rep_circ1 = Circle(radius= 0.3, color= WHITE).shift(5 * LEFT)
        rep_circ2 = Circle(radius= 0.3, color= WHITE).shift(4 * LEFT)
        rep_circ3 = Circle(radius= 0.3, color= WHITE).shift(3 * LEFT)
        rep_circ4 = Circle(radius= 0.3, color= WHITE).shift(2 * LEFT)
        rep_circ5 = Circle(radius= 0.3, color= WHITE).shift(1 * LEFT)
        rep_circ6 = Circle(radius= 0.3, color= WHITE)
        rep_circ7 = Circle(radius= 0.3, color= WHITE).shift(1 * RIGHT)
        rep_acc = Circle(radius= 0.2, color= WHITE).shift(1 * RIGHT)
        unt_circ1 = Circle(radius= 0.3, color= WHITE).shift(5 * LEFT)
        unt_circ2 = Circle(radius= 0.3, color= WHITE).shift(4 * LEFT)
        unt_circ3 = Circle(radius= 0.3, color= WHITE).shift(3 * LEFT)
        unt_circ4 = Circle(radius= 0.3, color= WHITE).shift(2 * LEFT)
        unt_circ5 = Circle(radius= 0.3, color= WHITE).shift(1 * LEFT)
        unt_circ6 = Circle(radius= 0.3, color= WHITE)
        unt_circ7 = Circle(radius= 0.3, color= WHITE).shift(1 * RIGHT)
        unt_circ8 = Circle(radius= 0.3, color= WHITE).shift(2 * RIGHT)
        unt_circE = Circle(radius= 0.8, color= WHITE).shift(2 * DOWN).shift(2 * LEFT)
        loop_circ1 = Circle(radius= 0.7, color= WHITE).shift(3 * UP, 4 * LEFT)
        loop_circ2 = Circle(radius= 0.3, color= WHITE).shift(3 * UP).shift(2 * LEFT)
        loop_circ3 = Circle(radius= 0.3, color= WHITE).shift(3 * UP)
        loop_circ4 = Circle(radius= 0.7, color= WHITE)
        loop_circ5 = Circle(radius= 0.3, color= WHITE).shift(2 * RIGHT, 3 * UP)
        loop_circ6 = Circle(radius= 0.3, color= WHITE).shift(3 * RIGHT, 3 * UP)
        loop_circ7 = Circle(radius= 0.3, color= WHITE).shift(4 * RIGHT, 3 * UP)
        loop_circ8 = Circle(radius= 0.3, color= WHITE).shift(5 * RIGHT, 3 * UP)
        loop_circ9 = Circle(radius= 0.3, color= WHITE).shift(5 * RIGHT)
        loop_circ10 = Circle(radius= 0.3, color= WHITE).shift(4 * RIGHT, 1 * DOWN)
        dfa_error = Circle(radius= 0.7, color= WHITE).shift(2.5 * DOWN)

        circs = [rep_circ1, rep_circ2, rep_circ3, rep_circ4, rep_circ5, rep_circ6, rep_circ7, rep_acc, dfa_error]
        unt_circs = [unt_circ1, unt_circ2, unt_circ3,
                     unt_circ4, unt_circ5, unt_circ6,
                     unt_circ7, unt_circ8, dfa_error]
        loop_circs = [loop_circ1, loop_circ2, loop_circ3, loop_circ4, loop_circ5, loop_circ6, loop_circ7, loop_circ8, loop_circ9, loop_circ10, dfa_error]


        #repeat state numbers
        state1 = center_text("1", rep_circ1)
        state2 = center_text("2", rep_circ2)
        state3 = center_text("3", rep_circ3)
        state4 = center_text("4", rep_circ4)
        state5 = center_text("5", rep_circ5)
        state6 = center_text("6", rep_circ6)
        state7 = center_text("7", rep_acc)
        state_error = center_text("Error", dfa_error)
        unt_state1 = center_text("1",     unt_circ1)
        unt_state2 = center_text("2",     unt_circ2)
        unt_state3 = center_text("3",     unt_circ3)
        unt_state4 = center_text("4",     unt_circ4)
        unt_state5 = center_text("5",     unt_circ5)
        unt_state6 = center_text("6",     unt_circ6)
        unt_state7 = center_text("ID",    unt_circ7)
        unt_state8 = center_text("8",     unt_circ8)
        unt_stateE = center_text("ERROR", unt_circE)
        loop_state1 = center_text("repeat", loop_circ1)
        loop_state2 = center_text("8", loop_circ2)
        loop_state3 = center_text("9", loop_circ3)
        loop_state4 = center_text("until", loop_circ4)
        loop_state5 = center_text("error", dfa_error)
        loop_state6 = center_text("10", dfa_error)
        loop_state7 = center_text("11", dfa_error)
        loop_state8 = center_text("12", dfa_error)
        loop_state9 = center_text("13", dfa_error)
        loop_state9 = center_text("14", dfa_error)
        loop_states = [loop_state1, loop_state2, loop_state3, loop_state4, loop_state5, loop_state6, loop_state7, loop_state8, loop_state9, loop_state9]

        states = [state1, state2, state3,
                  state4, state5, state6,
                  state7, state_error]
        unt_states = [unt_state1, unt_state2, unt_state3,
                      unt_state4, unt_state5, unt_state6,
                      unt_state7, unt_state8, unt_stateE]


        #repeat arrows
        arrow_12 = drawArrows(rep_circ1, right, rep_circ2, left, 0, 0.2)
        arrow_23 = drawArrows(rep_circ2, right, rep_circ3, left, 0, 0.2)
        arrow_34 = drawArrows(rep_circ3, right, rep_circ4, left, 0, 0.2)
        arrow_45 = drawArrows(rep_circ4, right, rep_circ5, left, 0, 0.2)
        arrow_56 = drawArrows(rep_circ5, right, rep_circ6, left, 0, 0.2)
        arrow_67 = drawArrows(rep_circ6, right, rep_circ7, left, 0, 0.2)
        arrow_77 = drawArrows(rep_circ7, up, rep_circ7, right, -TAU/2, 0.2)
        arrow_19 = drawArrows(rep_circ1, down, dfa_error, up, TAU/4, 0.2)
        arrow_29 = drawArrows(rep_circ2, down, dfa_error, up, TAU/4, 0.2)
        arrow_39 = drawArrows(rep_circ3, down, dfa_error, up, TAU/4, 0.2)
        arrow_49 = drawArrows(rep_circ4, down, dfa_error, up, TAU/4, 0.2)
        arrow_59 = drawArrows(rep_circ5, down, dfa_error, up, TAU/4, 0.2)
        arrow_69 = drawArrows(rep_circ6, down, dfa_error, up, TAU/4, 0.2)
        arrow_99 = drawArrows(dfa_error, right, dfa_error, down, -TAU/2, 0.2)
        unt_arrow_12 = drawArrows(unt_circ1, right, unt_circ2, left, 0, 0.2)
        unt_arrow_23 = drawArrows(unt_circ2, right, unt_circ3, left, 0, 0.2)
        unt_arrow_34 = drawArrows(unt_circ3, right, unt_circ4, left, 0, 0.2)
        unt_arrow_45 = drawArrows(unt_circ4, right, unt_circ5, left, 0, 0.2)
        unt_arrow_56 = drawArrows(unt_circ5, right, unt_circ6, left, 0, 0.2)
        unt_arrow_67 = drawArrows(unt_circ6, right, unt_circ7, left, 0, 0.2)
        unt_arrow_78 = drawArrows(unt_circ7, right, unt_circ8, left, 0, 0.2)
        unt_arrow_88 = drawArrows(unt_circ8, right, unt_circ8, down, -TAU/2, 0.2)
        unt_arrow_1E = drawArrows(unt_circ1, down, unt_circE, left, TAU/4 , 0.2)
        unt_arrow_2E = drawArrows(unt_circ2, down, unt_circE, left, TAU/4 , 0.2)
        unt_arrow_3E = drawArrows(unt_circ3, down, unt_circE, left, TAU/4 , 0.2)
        unt_arrow_4E = drawArrows(unt_circ4, down, unt_circE, up, 0, 0.2)
        unt_arrow_5E = drawArrows(unt_circ5, down, unt_circE, right, -TAU/4 , 0.2)
        unt_arrow_6E = drawArrows(unt_circ6, down, unt_circE, right, -TAU/4 , 0.2)
        unt_arrow_7E = drawArrows(unt_circ7, down, unt_circE, right, -TAU/4 , 0.2)
        loop_arrow_R2 = drawArrows(loop_circ1, right, loop_circ2, left, 0, 0.2)
        loop_arrow_22 = drawArrows(loop_circ2, left, loop_circ2, up, -TAU/2, 0.2)
        loop_arrow_23 = drawArrows(loop_circ2, right, loop_circ3, left, 0, 0.2)
        loop_arrow_32 = drawArrows(loop_circ3, up, loop_circ2, right, TAU/4, 0.2)
        loop_arrow_3U = drawArrows(loop_circ3, down, loop_circ4, up, 0, 0.2)
        loop_arrow_2E = drawArrows(loop_circ2, down, dfa_error, left, TAU/4, 0.2)
        loop_arrow_RE = drawArrows(loop_circ1, down, dfa_error, left, TAU/4, 0.2)
        loop_arrow_34 = drawArrows(loop_circ3, down, dfa_error, left, TAU/4, 0.2)
        loop_arrow_45 = drawArrows(loop_circ5, down, dfa_error, left, TAU/4, 0.2)
        loop_arrow_56 = drawArrows(loop_circ6, down, dfa_error, left, TAU/4, 0.2)
        loop_arrow_77 = drawArrows(loop_circ7, down, dfa_error, left, TAU/4, 0.2)
        
        pointer = CurvedArrow(angle=0,start_point=squares[0].get_top() + 0.5 * UP, end_point=squares[0].get_top(), tip_length=0.2, color=WHITE)

        arrows = [arrow_12, arrow_23,
                  arrow_34, arrow_45,
                  arrow_56, arrow_67,
                  arrow_19, arrow_29,
                  arrow_39, arrow_49,
                  arrow_59, arrow_69,
                  arrow_77, arrow_99]

        unt_arrows = [unt_arrow_12, unt_arrow_23,
                      unt_arrow_34, unt_arrow_45,
                      unt_arrow_56, unt_arrow_67,
                      unt_arrow_78, unt_arrow_88,
                      unt_arrow_1E, unt_arrow_5E,
                      unt_arrow_2E, unt_arrow_6E,
                      unt_arrow_3E, unt_arrow_7E,
                      unt_arrow_4E,]
        loop_arrows = [loop_arrow_R2, loop_arrow_22, loop_arrow_22,
                       loop_arrow_23, loop_arrow_32, loop_arrow_3U,
                       loop_arrow_2E, loop_arrow_RE]


        
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

        arrows_text = [rep_txt_12,rep_txt_23,rep_txt_34,
                       rep_txt_45, rep_txt_56,rep_txt_67,
                       rep_txt_77, rep_txt_19,rep_txt_29,
                       rep_txt_39,rep_txt_49, rep_txt_59,
                       rep_txt_69, rep_txt_99]

        unt_arrows_text = [unt_txt_12, unt_txt_23, unt_txt_34,
                           unt_txt_45, unt_txt_56, unt_txt_67,
                           unt_txt_78, unt_txt_88, unt_txt_1E,
                           unt_txt_2E, unt_txt_3E, unt_txt_4E,
                           unt_txt_5E, unt_txt_6E, unt_txt_7E]

        loop_arrows_text = [loop_text_R2, loop_text_32,
                            loop_text_22, loop_text_23,
                            loop_text_3U, loop_text_2E,
                            loop_text_RE]

        for t in range(len(text)):
            text[t].move_to(squares[t].get_center()).scale(0.8)

        reset_cir(circs)
        # self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.1), FadeIn(pointer), AnimationGroup(*[FadeIn(t) for t in text], lag_ratio=0.1))
        # self.play(Create(VGroup(*circs, *states, *arrows, *arrows_text)), run_time = 9)
        # self.play(Create(VGroup(*unt_circs, *unt_states, *unt_arrows, *unt_arrows_text)), run_time = 9)
        self.play(Create(VGroup(*loop_circs, *loop_states, *loop_arrows, *loop_arrows_text)), run_time = 2)
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
