def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    df = df.copy()

    # Ensure numeric conversion
    df["pH"] = pd.to_numeric(df["pH"], errors="coerce")
    df["turbidity"] = pd.to_numeric(df["turbidity"], errors="coerce")

    # Drop rows where pH or turbidity is missing
    df = df.dropna(subset=["pH", "turbidity"])

    return df
