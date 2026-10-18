package utils

import (
	"strconv"
	"strings"
	"unicode/utf8"
)

func FormatKopeks(kopeks int) string {
	rubles := strconv.Itoa(kopeks / 100)
	var groups []string
	for len(rubles) > 3 {
		groups = append([]string{rubles[len(rubles)-3:]}, groups...)
		rubles = rubles[:len(rubles)-3]
	}
	groups = append([]string{rubles}, groups...)
	cents := kopeks % 100
	return strings.Join(groups, " ") + "," + cents + " ₽"
}

func FormatTitle(text string, width int) string {
	free := width - utf8.RuneCountInString(text)
	if free <= 0 {
		return text
	}
	left := free / 2
	return strings.Repeat("=", left) + text + strings.Repeat("=", free-left)
}
