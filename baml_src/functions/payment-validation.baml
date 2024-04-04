function PaymentValidation {
    input string
    output PaymentValidationData
}

class ExactPaymentData {
    exactAmount float
    quote string
}

class EstimatePaymentData {
    estimateAmount float
    quote string
}

class ReceivedPaymentData {
    paymentNotReceived bool
    quote string
}

class PaymentValidationData2 {
    estimate string? @description("Only set if the payment refers to an estimate but not an exact guidance.  Future work is always an estimate.")
    exact float? @description("If the email is outlining exactly what the final payment due is.")
    notReceived string? @description("The exact quote in the email explicitly stating a previously requested payment has not been received yet.")
}

class PaymentValidationData {
    presentPayment float? @description("If the agency is asking for a payment to be made now to fulfill the current request - include estimates which must be paid before they will begin working on the request.")
    futurePayment float? @description("If the agency is giving an estimate or advanced notice for an amount which will be due in the future, and does not need to be made now.")
    notReceived bool @description("Is the agency stating they have not yet received payment which was previously asked for.  This should only be true for follow ups to previous requests for payment or invoices, and not for new payment requests.")
}

impl<llm, PaymentValidation> v1 {
    client GPT4Client

    prompt #"
        Given this email extract any payment related content

        ###
        {#input}
        ###

        OUTPUT FORMAT:
        {#print_type(output)}

        Before OUTPUT FORMAT, summarize all the payment related content.
        Example: 
        <summary...>
        {
            ...
        }
    "#
}


