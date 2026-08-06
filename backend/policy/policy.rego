package healthcare.prior_auth

default allow := false
default escalate := false

allow if {
    input.estimated_cost <= 5000
}

escalate if {
    input.estimated_cost > 5000
}

decision := "APPROVE" if {
    allow
}

decision := "ESCALATE" if {
    escalate
}

reasons := ["Auto-approved"] if {
    allow
}

reasons := ["Amount exceeds approval threshold"] if {
    escalate
}