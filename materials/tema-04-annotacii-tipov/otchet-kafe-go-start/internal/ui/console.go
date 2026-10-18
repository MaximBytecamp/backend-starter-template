package ui

import "fmt"

func PrintReport(lines []string) {
	for _, line := range lines {
		fmt.Println(line)
	}
}
