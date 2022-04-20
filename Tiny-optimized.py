from manim import *
from manim.opengl import *

class State():
    def __init__(self, id, circle, state_text):
        self.id         = id
        self.circle     = circle
        self.state_text = state_text

class Edge():
    def __init__(self, arrow, state_v, transition):
        self.arrow      = arrow
        self.state_v    = state_v
        self.transition = transition

class Tiny(Scene):
    def construct(self):
        def draw_state(state):
            txt = Text(state.state_text).set_color(WHITE)
            txt.move_to(state.circle.get_center()).scale(0.3)

            # self.play(Create(VGroup(state.circle, txt)), run_time=0.005)
            self.add(state.circle, txt)

        def draw_states(circles):
            for cir in circles:
                draw_state(cir)

        def draw_arrow(edge): 
            txt = Text(edge.transition).set_color(YELLOW)
            txt.move_to(edge.arrow.get_midpoint()).scale(0.2).shift(0.1 * UP)

            self.play(Create(VGroup(edge.arrow, txt)), run_time=0.005)

        def draw_arrows(arrows):
            for arrow in arrows:
                draw_arrow(arrow)

        def read_states():
            return_list = []
            with open('states.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    attrs = line.split()
                    cir_obj = Circle(radius=float(attrs[1]), color=eval(attrs[2]))
                    cir_obj.shift(float(attrs[4]) * UP).shift((float(attrs[3]) * RIGHT))

                    return_list.append(State(len(return_list) + 1, cir_obj, attrs[0]))

            return return_list

        def read_arrows(states, edges):
            return_list = []
            with open('arrows.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    attrs = line.split()

                    state_u = states[int(attrs[0]) - 1]
                    state_v = states[int(attrs[1]) - 1]
                    start = eval(f'state_u.circle.get_{attrs[3]}()')
                    end   = eval(f'state_v.circle.get_{attrs[4]}()')

                    arrow = CurvedArrow(angle=float(attrs[5]), start_point=start,
                                        end_point=end, tip_length=0.1, color=LIGHT_BROWN)

                    edge = Edge(arrow, state_v, attrs[2])
                    return_list.append(edge)

                    state = int(attrs[0])
                    if state not in edges:
                        edges[state] = dict()

                    edges[state][attrs[2]] = edge
            
            return return_list

        def is_letter_or_num(ch):
            return ch.isalnum()

        def is_equal_lt_gt(ch):
            return ch in '=<>'

        def is_letter(ch):
            return ch.isalpha()

        def is_num(ch):
            return ch.isnumeric()

        def is_space(ch):
            return ch == ' '

        def is_ws(ch):
            return ch.isspace()

        def match_single(transition, ch):
            if transition == 'any':
                return True
            # ch
            elif len(transition) == 1:
                return transition[0] == ch
            # ~ch
            elif transition[0] == '~' and len(transition) == 2:
                return ch != transition[1]
            elif transition[0] == '~':
                return not eval(f'is_{transition[1:]}(ch)')
            else:
                is_equal_lt_gt(ch)
                is_letter(ch)
                is_space(ch)
                is_ws(ch)
                is_num(ch)
                return eval(f'is_{transition}(ch)')

        def match(transition, ch):
            if transition == 'letter,num':
                return is_letter_or_num(ch)
            elif transition == '=,<,>':
                return is_equal_lt_gt(ch)
            else:
                conditions = transition.split(',')
                return all([match_single(condition, ch) for condition in conditions])

        def get_next_transition(possible_transitions, ch):
            for transition in possible_transitions:
                if match(transition, ch):
                    return transition

        states = read_states()
        edges  = dict()
        def play_animation(input_text):
            cur_state = 1
            for char in input_text[0:len(input_text)-1]:
                next_transition = get_next_transition(edges[cur_state].keys(), char)
                edge            = edges[cur_state][next_transition]
                next_circle     = edge.state_v.circle
                orig_color_cir  = next_circle.color
                orig_color_edg  = edge.arrow.color
                print(repr(char), cur_state, next_transition, edge.state_v.state_text)

                edge.arrow.set_color(GREEN)
                next_circle.set_color(GREEN)

                self.play(edge.arrow.animate, next_circle.animate, run_time=1)

                edge.arrow.set_color(orig_color_edg)
                next_circle.set_color(orig_color_cir)

                cur_state = edge.state_v.id
                
        draw_states(states)
        draw_arrows(read_arrows(states, edges))

        print(is_letter('x'))
        file_name = 'accept1.txt'
        with open(file_name, 'r') as file:
            data = file.read()
            print(repr(data))
            play_animation(data)

