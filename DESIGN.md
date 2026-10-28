# Research Data Checker — Design

## Purpose and users

- Help researchers identify potentially problematic measurements in CSV files before analysis.


## Expected behaviour

- Read a CSV file containing a numeric column named `measurement`.
- Check measurements against minimum and maximum limits.
- Accept optional `--minimum` and `--maximum` command-line arguments.
- Default to a minimum of `0` and a maximum of `100`.
- If only one limit is supplied, retain the default for the other.
- Treat measurements equal to either limit as valid.
- Report measurements outside the limits without modifying the CSV.
- Reject a minimum greater than the maximum with a clear error message.

## Constraints and assumptions

- Preserve existing behaviour when no limits are supplied.
- Keep the implementation focused on configurable measurement limits.
- Avoid unrelated changes or additional dependencies.
- Report problems rather than automatically correcting data.

## Open questions

The following are outside the scope of the current feature:

- How should missing, non-numeric and non-finite measurements be classified?
- Should future versions support multiple measurement columns?

git status
git diff  # unstaged changes
git log --oneline --graph --all

git switch -c my-changes

