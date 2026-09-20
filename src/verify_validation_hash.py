from pathlib import Path
import hashlib
import pandas as pd

EXPECTED_SHA256 = "9ef9796b30ed6695f501bd330547b8c9b16c00abfe7ad1675d91b99b2a27a29a"
CSV_PATH = Path(__file__).resolve().parents[1] / "validation" / "single_scenario_results_validation_merged_120.csv"

df = pd.read_csv(CSV_PATH)
canonical = df.drop(columns=["source_file"], errors="ignore")
payload = canonical.to_csv(index=False).encode("utf-8")
actual = hashlib.sha256(payload).hexdigest()

print("Rows:", len(canonical))
print("Unique configurations:", canonical["configuration_id"].nunique())
print("SHA-256:", actual)
if actual != EXPECTED_SHA256:
    raise SystemExit("FAIL: validation-table fingerprint mismatch")
print("PASS: validation-table fingerprint matches the frozen-selection record")
