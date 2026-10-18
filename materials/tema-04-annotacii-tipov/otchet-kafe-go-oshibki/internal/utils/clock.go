package utils

import "time"

func TodayLabel() string {
	return time.Now().Format("02.01.2006")
}
