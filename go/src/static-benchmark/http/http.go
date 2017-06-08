package main

import (
	"log"
	"net/http"
	"runtime"
	"path"
	"fmt"
	"time"
)

func main() {
	_, filename, _, ok := runtime.Caller(0)
	if !ok {
		panic("No caller information")
	}
	var static = path.Join(path.Dir(path.Dir(path.Dir(path.Dir(path.Dir(filename))))),"assets")

	s := &http.Server{
		Addr:           ":4000",
		Handler:        http.StripPrefix("/assets/", http.FileServer(http.Dir(static))),
		ReadTimeout:    30 * time.Second,
		WriteTimeout:   30 * time.Second,
		MaxHeaderBytes: 1 << 20,
	}

	fmt.Printf("running on port 4000 serving %q\n", static)
	log.Fatal(s.ListenAndServe())
}