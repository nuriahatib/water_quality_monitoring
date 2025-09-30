class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series):
        """
        Determine if a row of water data is safe.
        Returns:
            tuple: (bool, str) Safe status and reason.
        """
        if pd.isna(row["pH"]):
            return False, "missing pH"
        if pd.isna(row["turbidity"]):
            return False, "missing turbidity"

        if not (self.ph_range[0] <= row["pH"] <= self.ph_range[1]):
            return False, "pH out of range"
        if row["turbidity"] > self.turbidity_threshold:
            return False, "turbidity too high"

        return True, "Safe"
