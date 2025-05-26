from manim import *


class Ref(Scene):
    def construct(self):
        # writing in the title
        title = Title("Solving Systems of E.Q.'s with REF/RREF")
        self.play(Write(title))

        # writing in the systems and highlighting both coefficients and constants
        system = MathTex(r"\begin{cases} 1x + 2y = 5 \\ 3x + 4y = 11 \end{cases}")
        self.play(Write(system))
        self.play(
            system[0][1].animate.set_color(YELLOW),
            system[0][4].animate.set_color(YELLOW),
            system[0][8].animate.set_color(YELLOW),
            system[0][11].animate.set_color(YELLOW),
            run_time=0.01,
        )
        self.play(
            system[0][7].animate.set_color(BLUE),
            system[0][14].animate.set_color(BLUE),
            system[0][15].animate.set_color(BLUE),
            run_time=0.01,
        )
        self.wait(1)
        linear_combination = MathTex(
            r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 11 \end{bmatrix}"
        )
        linear_combination[0][1].set_color(YELLOW)
        linear_combination[0][2].set_color(YELLOW)
        linear_combination[0][3].set_color(YELLOW)
        linear_combination[0][4].set_color(YELLOW)
        linear_combination[0][12].set_color(BLUE)
        linear_combination[0][13:15].set_color(BLUE)

        lc_caption = MathTex(r"A\vec{x} = \vec{b} \text{ form}")
        lc_caption.next_to(linear_combination, DOWN, buff=0.25)

        self.play(FadeOut(system))
        self.wait(0.25)
        self.play(Write(linear_combination), Write(lc_caption))
        self.wait()
