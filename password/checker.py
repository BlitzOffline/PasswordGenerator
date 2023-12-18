import zxcvbn


class PasswordChecker:
    @staticmethod
    def strength_check(password: str, user_input: set[str] = None):
        result = zxcvbn.zxcvbn(password=password, user_inputs=user_input)

        score = None
        warning = None
        suggestions = None
        crack_times_display = None

        if "score" in result:
            score = result.pop("score")
        if "feedback" in result:
            feedback = result.pop("feedback")
            if "warning" in feedback:
                warning = feedback.pop("warning")
            if "suggestions" in feedback:
                suggestions = feedback.pop("suggestions")
        if "crack_times_display" in result:
            crack_times_display = result.pop("crack_times_display")
            if "online_no_throttling_10_per_second" in crack_times_display:
                crack_times_display = crack_times_display.pop("online_no_throttling_10_per_second")

        return score, warning, suggestions, crack_times_display
