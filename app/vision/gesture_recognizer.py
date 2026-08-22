import math


class GestureRecognizer:

    def _distance(self, a, b):
        return math.sqrt(
            (a.x - b.x) ** 2 +
            (a.y - b.y) ** 2
        )

    def recognize(self, hand_landmarks):

        if not hand_landmarks:
            return "NO_HAND"

        # -----------------------------------------
        # Landmark references
        # -----------------------------------------

        wrist = hand_landmarks[0]

        thumb_tip = hand_landmarks[4]
        thumb_ip = hand_landmarks[3]
        thumb_mcp = hand_landmarks[2]

        index_tip = hand_landmarks[8]
        index_pip = hand_landmarks[6]

        middle_tip = hand_landmarks[12]
        middle_pip = hand_landmarks[10]

        ring_tip = hand_landmarks[16]
        ring_pip = hand_landmarks[14]

        pinky_tip = hand_landmarks[20]
        pinky_pip = hand_landmarks[18]

        # -----------------------------------------
        # Finger detection
        # -----------------------------------------

        index_open = self._distance(index_tip, wrist) > \
                     self._distance(index_pip, wrist)

        middle_open = self._distance(middle_tip, wrist) > \
                      self._distance(middle_pip, wrist)

        ring_open = self._distance(ring_tip, wrist) > \
                    self._distance(ring_pip, wrist)

        pinky_open = self._distance(pinky_tip, wrist) > \
                     self._distance(pinky_pip, wrist)

        # -----------------------------------------
        # Thumb detection
        # -----------------------------------------

        thumb_extended = self._distance(
            thumb_tip,
            wrist
        ) > self._distance(
            thumb_mcp,
            wrist
        ) * 1.25

        # -----------------------------------------
        # THUMBS UP
        # -----------------------------------------
        #
        # Thumb extended
        # Other four fingers folded
        #

        if (
            thumb_extended
            and not index_open
            and not middle_open
            and not ring_open
            and not pinky_open
            and thumb_tip.y < thumb_mcp.y
        ):
            return "THUMBS_UP"

        # -----------------------------------------
        # VICTORY / PEACE ✌️
        # -----------------------------------------
        if (
            index_open
            and middle_open
            and not ring_open
            and not pinky_open
        ):
            return "VICTORY"

        # -----------------------------------------
        # OPEN PALM
        # -----------------------------------------
        if (
            index_open
            and middle_open
            and ring_open
            and pinky_open
        ):
            return "OPEN_PALM"

        # -----------------------------------------
        # FIST
        # -----------------------------------------
        if (
            not index_open
            and not middle_open
            and not ring_open
            and not pinky_open
            and not thumb_extended
        ):
            return "FIST"

        return "UNKNOWN"