package services

import (
	"os"
	"strings"
)

func SaveReport(path string, lines []string) (int, error) {
	err := os.WriteFile(path, strings.Join(lines, "\n"), 0o644)
	if err != nil {
		return 0, err
	}
	return len(lines), nil
}
