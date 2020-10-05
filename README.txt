SteamFitter


    Goal: Identify extra pipes in a .tsv file.
    DONE!:    Phase 1: Identify lines with addtional pipes and output line number to console
            - example: 34
            - test: File open, read lines, output == expected test dat.

        Phase 2: Add functionality to identify pipes inside of quotes with >> <<
            - example: Console Out ->  Line 34  ..."Manager >>|<< Investor"...
        
        Phase 3: Add funcitonality so that program prompts user to delete pipe and replace w/ space or keep pipe
            - example: Console out -> Line 34..."Manager >>|<< Investor "...
                - Do you wish to delete pipe? (y/n): y
                - if yes: Pipe has been deleted
                - if no: Pipe has not been deleted
        
        Phase 4: Add flag capabilities to define number of pipes
        - '-p' int(number of pipes expected)
                - SteamFitter example.tsv -p 5
                    - expected number of pipes per line in example.tsv is 5
        
        Phase 5: Add flag if file is headerless
        - '-h' 

        Phase 6: Add flag that converts .tsv to .csv
        - '-c'
