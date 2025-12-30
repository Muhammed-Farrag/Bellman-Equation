from manim import *

class BellmanDerivation(Scene):
    def construct(self):
        # 0. Slogan / Watermark
        watermark = Text("STITCH", font_size=30, color=GREY, font="Luminari").to_corner(DR).set_opacity(0.5)
        self.add(watermark)
        # ==========================================
        # SECTION 1: Expected Return (G_t)
        # ==========================================
        
        # 1. Define Return G_t (Discounted sum of rewards)
        g_t_text = MathTex(
            r"G_t", r"=", r"R_{t+1}", r"+", r"\gamma R_{t+2}", r"+", r"\gamma^2 R_{t+3}", r"+ \dots"
        )
        g_t_text.scale(1.2)
        
        title_1 = Text("1. The Goal: Expected Return").to_edge(UP).scale(0.8)
        
        self.play(Write(title_1))
        self.play(Write(g_t_text))
        self.wait(1)

        # 2. Group future terms (Recursive definition)
        brace_future = Brace(g_t_text[4:], DOWN)
        future_text = brace_future.get_text(r"$\gamma G_{t+1}$")
        
        self.play(GrowFromCenter(brace_future), FadeIn(future_text))
        self.wait(1)

        # 3. Simplify to G_t = R + Gamma * G_{t+1}
        simple_g_t = MathTex(r"G_t", r"=", r"R_{t+1}", r"+", r"\gamma G_{t+1}")
        simple_g_t.scale(1.2)
        
        self.play(
            TransformMatchingTex(g_t_text, simple_g_t),
            FadeOut(brace_future), FadeOut(future_text)
        )
        self.wait(2)
        
        # Move up to make space
        self.play(
            simple_g_t.animate.to_edge(UP).scale(0.8),
            FadeOut(title_1)
        )

        # ==========================================
        # SECTION 2: The Value Function
        # ==========================================
        
        title_2 = Text("2. The Value Function").next_to(simple_g_t, DOWN, buff=0.5).scale(0.8)
        self.play(Write(title_2))

        # 1. Define Value as Expected Return
        value_def = MathTex(
            r"v_{\pi}(s)", r"=", r"\mathbb{E}_{\pi}", r"[", r"G_t", r"| S_t=s]"
        )
        self.play(Write(value_def))
        self.wait(1)

        # 2. Substitute G_t with recursive formula
        value_expanded = MathTex(
            r"v_{\pi}(s)", r"=", r"\mathbb{E}_{\pi}", r"[", 
            r"R_{t+1} + \gamma v_{\pi}(S_{t+1})", 
            r"| S_t=s]"
        )
        
        self.play(TransformMatchingTex(value_def, value_expanded))
        self.wait(2)

        # Clean up for the next big step
        self.play(
            FadeOut(title_2),
            FadeOut(simple_g_t),
            value_expanded.animate.to_edge(UP)
        )

        # ==========================================
        # SECTION 3: Bellman Expectation Equation
        # ==========================================
        
        title_3 = Text("3. The Bellman Expectation Equation").next_to(value_expanded, DOWN, buff=0.5).scale(0.8)
        self.play(Write(title_3))

        # Expand Expectation into Sum over Actions and Outcomes
        
        bellman_eq = MathTex(
            r"v_{\pi}(s)", r"=", 
            r"\sum_{a} \pi(a|s)", 
            r"\sum_{s', r} p(s',r|s,a)", 
            r"\left[", r"r", r"+", r"\gamma v_{\pi}(s')", r"\right]"
        )
        bellman_eq[2].set_color(BLUE)  # Policy
        bellman_eq[3].set_color(GREEN) # Dynamics
        
        self.play(ReplacementTransform(value_expanded, bellman_eq))
        self.wait(1)
        
        # Add labels to explain the parts
        brace_policy = Brace(bellman_eq[2], DOWN)
        txt_policy = brace_policy.get_text("Average over Actions").scale(0.5).set_color(BLUE)

        brace_dynamics = Brace(bellman_eq[3], UP)
        txt_dynamics = brace_dynamics.get_text("Average over Outcomes").scale(0.5).set_color(GREEN)

        self.play(GrowFromCenter(brace_policy), FadeIn(txt_policy))
        self.play(GrowFromCenter(brace_dynamics), FadeIn(txt_dynamics))
        self.wait(2)

        # ==========================================
        # SECTION 4: Bellman Optimality Equation
        # ==========================================
        
        # Change Average (Sum) to Max (Greedy)
        
        # Remove braces
        self.play(
            FadeOut(brace_policy), FadeOut(txt_policy),
            FadeOut(brace_dynamics), FadeOut(txt_dynamics),
            FadeOut(title_3)
        )
        
        title_4 = Text("4. The Bellman Optimality Equation").to_edge(UP).scale(0.8)
        self.play(Write(title_4))
        
        # The Transformation: Change Sum_a to Max_a
        # And v_pi to v_*
        optimality_eq = MathTex(
            r"v_{*}(s)", r"=", 
            r"\max_{a}", 
            r"\sum_{s', r} p(s',r|s,a)", 
            r"\left[", r"r", r"+", r"\gamma v_{*}(s')", r"\right]"
        )
        optimality_eq[2].set_color(RED) # Max
        optimality_eq[3].set_color(GREEN)

        self.play(TransformMatchingTex(bellman_eq, optimality_eq))
        
        # Highlight the MAX operator
        box = SurroundingRectangle(optimality_eq[2], buff=0.1, color=RED)
        max_label = Text("Greedy Choice!").next_to(box, DOWN).scale(0.5).set_color(RED)
        
        self.play(Create(box), Write(max_label))
        self.wait(3)

        # Final Cleanup
        self.play(FadeOut(Group(title_4, optimality_eq, box, max_label)))

        # ==========================================
        # SECTION 5: Numerical Example (State X)
        # ==========================================

        # 1. Setup the Scene
        ex_title = Text("Example: State X (From Lecture Slide 23)").to_edge(UP).scale(0.8)
        self.play(Write(ex_title))

        # 2. Draw the State Node X
        node_x = Circle(radius=0.6, color=WHITE).set_fill(BLACK, opacity=1).shift(UP*1)
        label_x = MathTex("X").move_to(node_x)
        
        self.play(DrawBorderThenFill(node_x), Write(label_x))
        
        # 3. Draw the Two Action Branches (A1 vs A2)
        # Branch Left (A1)
        arrow_left = Arrow(node_x.get_bottom(), node_x.get_bottom() + DL*2.5, buff=0.1, color=BLUE)
        label_a1 = MathTex("A_1").next_to(arrow_left, LEFT).scale(0.8).set_color(BLUE)
        reward_left = MathTex("r=+1").scale(0.7).next_to(arrow_left.get_center(), LEFT, buff=0.2).set_color(YELLOW)
        
        # Branch Right (A2)
        arrow_right = Arrow(node_x.get_bottom(), node_x.get_bottom() + DR*2.5, buff=0.1, color=BLUE)
        label_a2 = MathTex("A_2").next_to(arrow_right, RIGHT).scale(0.8).set_color(BLUE)
        reward_right = MathTex("r=0").scale(0.7).next_to(arrow_right.get_center(), RIGHT, buff=0.2).set_color(YELLOW)

        self.play(
            GrowArrow(arrow_left), Write(label_a1), Write(reward_left),
            GrowArrow(arrow_right), Write(label_a2), Write(reward_right)
        )
        self.wait(1)

        # 4. Show the Total Calculated Values (From Slide 23)
        # Left Outcome
        val_left_circle = Circle(radius=0.4, color=GREY).move_to(arrow_left.get_end())
        val_left_text = MathTex("5.3").scale(0.8).next_to(val_left_circle, DOWN)
        val_left_desc = Text("Total Value", font_size=20, color=GREY).next_to(val_left_text, DOWN)
        
        # Right Outcome
        val_right_circle = Circle(radius=0.4, color=GREY).move_to(arrow_right.get_end())
        val_right_text = MathTex("9.5").scale(0.8).next_to(val_right_circle, DOWN)
        val_right_desc = Text("Total Value", font_size=20, color=GREY).next_to(val_right_text, DOWN)

        self.play(
            Create(val_left_circle), Write(val_left_text), FadeIn(val_left_desc),
            Create(val_right_circle), Write(val_right_text), FadeIn(val_right_desc)
        )
        self.wait(1)

        # 5. Apply the Bellman Optimization (MAX operator)
        # "We compare 5.3 vs 9.5"
        
        comparison = MathTex(r"5.3 < 9.5").scale(1.5).shift(DOWN*0.5)
        self.play(Write(comparison))
        self.wait(1)
        
        # Highlight the Winner
        winner_rect = SurroundingRectangle(VGroup(val_right_circle, val_right_text), color=GREEN, buff=0.2)
        winner_label = Text("Optimal!", color=GREEN, font_size=24).next_to(winner_rect, RIGHT)
        
        self.play(
            Create(winner_rect), 
            Write(winner_label),
            comparison.animate.set_color(GREEN)
        )
        
        # 6. Final Conclusion for State X
        final_eq = MathTex(r"v_{*}(X) = 9.5").scale(1.2).to_edge(DOWN)
        
        self.play(
            ReplacementTransform(comparison, final_eq),
            FadeOut(arrow_left), FadeOut(label_a1), FadeOut(reward_left), FadeOut(val_left_circle), FadeOut(val_left_text), FadeOut(val_left_desc)
        )
        
        self.wait(3)

        # Final Cleanup
        self.play(
            FadeOut(ex_title),
            FadeOut(node_x), FadeOut(label_x),
            FadeOut(arrow_right), FadeOut(label_a2), FadeOut(reward_right), FadeOut(val_right_circle), FadeOut(val_right_text), FadeOut(val_right_desc),
            FadeOut(winner_rect), FadeOut(winner_label),
            FadeOut(final_eq),
            FadeOut(watermark)
        )