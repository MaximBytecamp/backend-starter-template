package main

import (
	"fmt"
	"log"

	"example.com/otchet-kafe/internal/services"
	"example.com/otchet-kafe/internal/ui"
	"example.com/otchet-kafe/internal/utils"
)

func buildReport(path string) ([]string, error) {
	orders, err := services.LoadOrders(path)
	if err != nil {
		return nil, err
	}
	revenue, err := services.RevenueByWaiter(orders)
	if err != nil {
		return nil, err
	}
	lines := []string{utils.FormatTitle(" Смена "+utils.TodayLabel()+" ", 40)}
	total := 0
	for _, row := range revenue {
		lines = append(lines, fmt.Sprintf("%-20s%20s", row.Waiter, utils.FormatKopeks(row.Kopeks)))
		total += row.Kopeks
	}
	lines = append(lines, utils.FormatTitle(" Итого "+utils.FormatKopeks(total)+" ", 40))
	return lines, nil
}

func main() {
	lines, err := buildReport("data/smena.csv")
	if err != nil {
		log.Fatal(err)
	}
	ui.PrintReport(lines)
}
