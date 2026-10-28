"""Starting example for Practical 4: add one failing test of your own."""

from research_check.checks import check_numeric_range


def test_measurement_inside_range_has_no_issues():
    rows = [{"measurement": "50"}]
    assert check_numeric_range(rows, "measurement", 0.0, 100.0) == []

def test_non_finite_measurement_is_invalid():
    rows = [{"measurement": "nan"}]
    issues = check_numeric_range(rows, "measurement", 0.0, 100.0)

    assert len(issues) == 1
    assert issues[0].kind == "invalid"

def test_positive_and_negative_infinity_are_invalid():
    rows = [{"measurement": "inf"}, {"measurement": "-inf"}]
    issues = check_numeric_range(rows, "measurement", 0.0, 100.0)

    assert len(issues) == 2
    assert [issue.kind for issue in issues] == ["invalid", "invalid"]

from research_check.checks import Issue, find_duplicates


def test_find_duplicates_returns_no_issues_for_empty_rows():
    assert find_duplicates([], "id") == []


def test_find_duplicates_returns_no_issues_when_values_are_unique():
    rows = [{"id": "a"}, {"id": "b"}]

    assert find_duplicates(rows, "id") == []


def test_find_duplicates_reports_each_repeat_with_its_row_number():
    rows = [{"id": "a"}, {"id": "b"}, {"id": "a"}, {"id": "a"}]

    assert find_duplicates(rows, "id") == [
        Issue("duplicate", "Duplicate id: a", 4),
        Issue("duplicate", "Duplicate id: a", 5),
    ]


def test_find_duplicates_compares_values_exactly():
    rows = [{"id": "a"}, {"id": "A"}, {"id": " a "}]

    assert find_duplicates(rows, "id") == []


def test_find_duplicates_treats_missing_keys_as_empty_strings():
    rows = [{}, {}]

    assert find_duplicates(rows, "id") == [
        Issue("duplicate", "Duplicate id: ", 3),
    ]