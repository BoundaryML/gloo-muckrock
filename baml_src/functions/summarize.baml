function Summarize {
  input string
  output string
}
 
impl<llm, Summarize> v1 { 
  client GPT35Client

  prompt #"
    Extract data from the following TEXT that is a request for public records from a government agency.

    EXAMPLE STRUCTURE:
    Overall summary of main text: 1-4 sentences.
    Overall summary of what the correspondence is about if it exists. Only include details about the public records request. No need to include the actual redacted records.
    Important dates: 
    Any pending fees: 
    Whether this agency can work on this request. If not, why not, and who may be able to work on it instead?
    Next step for this request:


    Agency's response to the request:
    ###
    {#input}
    ###

    Summary of agency's response:
  "#
}