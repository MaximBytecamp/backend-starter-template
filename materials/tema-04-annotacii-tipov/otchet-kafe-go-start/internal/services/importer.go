package services

import (
	"encoding/csv"
	"errors"
	"io"
	"iter"
	"os"
)

func ReadRows(path string) iter.Seq2[map[string]string, error] {
	return func(yield func(map[string]string, error) bool) {
		file, err := os.Open(path)
		if err != nil {
			yield(nil, err)
			return
		}
		defer file.Close()

		reader := csv.NewReader(file)
		header, err := reader.Read()
		if err != nil {
			yield(nil, err)
			return
		}
		for {
			record, err := reader.Read()
			if errors.Is(err, io.EOF) {
				return
			}
			if err != nil {
				yield(nil, err)
				return
			}
			row := make(map[string]string, len(header))
			for i, name := range header {
				row[name] = record[i]
			}
			if !yield(row, nil) {
				return
			}
		}
	}
}
