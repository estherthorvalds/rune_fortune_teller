"""
Keyword lists for categorizing user concerns in the Rune Fortune Teller.
Coded by Claude's Sonnet 4.5 and redesigned by the student.
Each list contains lemmatized forms of English words that indicate the user 
wants GUIDANCE about LOVE, HEALTH, or FINANCE topics.

Focus: Words that signal problems, concerns, questions, or domain-specific vocabulary.
"""

LOVE = [
    # Core relationship words
    "love", "romance", "romantic", "relationship", "partner", "boyfriend", "girlfriend",
    "husband", "wife", "spouse", "marriage", "marry", "wedding", "engagement",
    "engage", "engaged", "fiance", "fiancee", "date", "dating", "crush",
    "infatuation", "soulmate", "sweetheart", "lover", "beloved",
    
    # Relationship status and stages
    "single", "available", "meet", "meeting", "first-date",
    "casual", "serious", "exclusive", "committed", "commitment",
    "stable", "long-term", "forever", "future",
    "cohabitate", "move-in", "live-together",
    
    # Relationship dynamics
    "together", "togetherness", "bond", "connection",
    "connect", "attachment", "attach", "closeness",
    "distance", "distant", "separation", "separate",
    
    # Trust and honesty
    "trust", "honest", "honesty", "faithful", "loyalty", "loyal",
    "unfaithful", "cheat", "cheating", "affair", "betray", "betrayal",
    
    # Emotional states specific to relationships
    "heart", "heartbreak", "heartbroken", "hurt", "pain",
    "miss", "longing", "lonely", "loneliness",
    "rejection", "reject", "rejected", "unrequited",
    "jealous", "jealousy", "insecure", "insecurity",
    
    # Physical intimacy
    "kiss", "kissing", "hug", "hugging", "embrace", "cuddle", "cuddling",
    "intimacy", "intimate", "sex", "sexual", "sexuality",
    "touch", "touching", "hold", "holding", "caress",
    "sensual", "erotic", "arousal", "arouse", "bedroom",
    
    # Breakup and loss
    "breakup", "break-up", "split", "divorce", "divorced",
    "end", "ending", "over", "goodbye", "leave", "left",
    "loss", "lost", "grieve", "grieving", "grief",
    
    # Attraction and desire
    "attraction", "attractive", "attract", "desire",
    "passion", "passionate", "chemistry", "spark",
    "fall", "falling", "smitten", "enamored",
    
    # Communication in relationships
    "text", "texting", "call", "calling", "message",
    "conversation", "communicate", "communication",
    "respond", "response", "reply", "ignore", "ignoring", "ghost", "ghosting",
    
    # Affection and feelings
    "affection", "affectionate", "adore", "adoring",
    "cherish", "treasure", "precious", "special",
    
    # Relationship problems
    "problem", "trouble", "difficulty", "struggle",
    "complicate", "complicated", "complex", "confuse", "confusion",
    "uncertain", "uncertainty", "doubt", "doubting",
    "concern", "concerned", "worry", "worried",
    "stress", "stressed", "pressure", "tension",
    "frustration", "frustrated", "upset",
    "fight", "fighting", "argue", "argument", "conflict", "disagreement",
    
    # Qualities in partners
    "handsome", "beautiful", "pretty", "gorgeous", "cute", "sexy",
    "funny", "humor", "intelligent", "smart",
    "confident", "confidence", "genuine", "authentic", "sincere",
    "warm", "warmth", "gentle", "protective",
    "dependable", "reliable", "mature", "responsible",
    
    # Actions and gestures
    "flirt", "flirting", "seduce", "seduction", "charm", "charming",
    "compliment", "surprise", "gift", "present", "flower",
    "dinner", "movie", "romantic-dinner",
    
    # Understanding and support
    "listen", "listening", "support", "supportive",
    "understand", "understanding", "appreciate", "appreciation",
    "grateful", "gratitude", "forgive", "forgiveness",
    "apologize", "apology", "sorry", "compromise", "resolve",
    
    # Dating and modern relationships
    "app", "dating-app", "tinder", "bumble", "match", "swipe", "profile", "online-dating",
    "talking", "situationship", "vibe", "click",
    "compatible", "compatibility", "red-flag", "green-flag",
    
    # Commitment and future
    "promise", "vow", "pledge", "commit",
    "devote", "devoted", "devotion", "dedication", "dedicate",
    "faithful", "fidelity", "monogamous", "monogamy",
    "partnership", "always", "eternal", "permanent", "lasting", "endure",
    
    # Family and children
    "family", "child", "children", "baby", "parent", "parenting",
    "pregnancy", "pregnant", "marry",
    
    # Affection terms
    "babe", "baby", "sweetie", "honey", "darling", "dear",
    
    # Emotional vulnerability
    "vulnerable", "vulnerability", "open", "share", "reveal", "expose",
    
    # Romance and passion
    "spark", "magic", "chemistry", "destiny", "fate",
    "soul", "soulmate", "spirit",
    
    # Milestones
    "anniversary", "proposal", "propose", "ring", "engaged",
    "first-kiss", "meet-parents", "honeymoon",
    
    # Hopes and seeking
    "hope", "hoping", "wish", "wishing", "dream", "dreaming",
    "search", "searching", "seek", "seeking", "find", "finding",
    
    # Relationship anxieties
    "overthink", "overthinking", "anxious", "anxiety", "nervous",
    "afraid", "insecure",
    
    # Positive emotions
    "happy", "happiness", "joy", "joyful", "excite", "excited", "excitement",
    
    # Modern dating issues
    "breadcrumb", "breadcrumbing", "bench", "benching",
    "slow-fade", "cushion", "cushioning",
    
    # Reconciliation and healing
    "heal", "healing", "recover", "recovery", "closure",
    "let-go", "release", "move-on"
]

HEALTH = [
    # General health and wellness
    "health", "healthy", "unhealthy", "wellness", "wellbeing", "fitness", "fit",
    "medical", "medicine", "doctor", "physician", "nurse", "hospital", "clinic",
    "appointment", "checkup", "exam", "examination", "visit",
    "on-call", "operating-room", "bay", "trauma-bay",
    
    # Symptoms and feeling unwell
    "sick", "sickness", "illness", "ill", "unwell",
    "pain", "painful", "ache", "aching", "hurt", "hurting", "sore", "soreness",
    "discomfort", "symptom", "suffer", "suffering",
    "shake", "shaking", "shaky", "tremor", "tremble",
    "race", "racing", "rapid",
    
    # Specific symptoms
    "fever", "temperature", "cough", "coughing", "cold", "flu",
    "headache", "migraine", "nausea", "nauseous", "vomit", "vomiting",
    "diarrhea", "constipation", "constipated",
    "fatigue", "fatigued", "tired", "exhaustion", "exhausted",
    "weakness", "weak", "dizzy", "dizziness", "faint", "fainting",
    "swelling", "swollen", "inflammation", "inflamed",
    "rash", "itch", "itching", "itchy",
    "bleed", "bleeding", "blood", "bruise", "bruising",
    
    # Injuries
    "injury", "injured", "injure", "wound", "wounded",
    "fracture", "fractured", "break", "broken", "broke",
    "sprain", "sprained", "strain", "strained", "tear", "torn",
    "cut", "laceration", "burn", "burned", "burnt",
    
    # Body parts (when discussing health issues)
    "head", "brain", "eye", "ear", "nose", "throat", "mouth", "tooth", "teeth",
    "neck", "shoulder", "arm", "elbow", "wrist", "hand", "finger",
    "chest", "heart", "lung", "stomach", "abdomen", "belly",
    "liver", "kidney", "intestine", "bowel", "bladder",
    "back", "spine", "hip", "leg", "knee", "ankle", "foot", "feet", "toe",
    "muscle", "bone", "joint", "nerve", "skin",
    
    # Medical diagnosis and treatment
    "diagnosis", "diagnose", "diagnosed", "test", "testing",
    "treatment", "treat", "cure", "heal", "healing",
    "recovery", "recover", "recovering", "rehabilitation", "rehabilitate",
    "therapy", "therapist", "physical-therapy",
    "intubate", "intubated", "intubation",
    "neuro", "neurology", "neurological",
    "consult", "consultation",
    "icp", "intracranial-pressure",
    "monitor", "monitoring", "monitored",
    "herniation", "herniate",
    "atls", "protocol", "protocols",
    "scanner", "triage", "morbidity",
    "preventable", "prevent", "prevention", "preventing",
    
    # Diseases and conditions
    "disease", "condition", "disorder", "syndrome",
    "infection", "infected", "virus", "viral", "bacteria", "bacterial",
    "cancer", "cancerous", "tumor", "mass", "malignant", "benign",
    "diabetes", "diabetic", "hypertension", "high-blood-pressure",
    "cholesterol", "heart-disease", "stroke", "heart-attack",
    "asthma", "allergy", "allergic", "arthritis", "osteoporosis",
    "chronic", "acute", "autoimmune",
    
    # Mental health
    "mental-health", "depression", "depressed", "anxiety", "anxious",
    "stress", "stressed", "panic", "panic-attack",
    "bipolar", "schizophrenia", "ptsd", "trauma", "traumatic",
    "ocd", "adhd", "add", "autism",
    "eating-disorder", "anorexia", "bulimia",
    "therapy", "therapist", "counseling", "counselor",
    "psychologist", "psychiatrist", "psychiatric",
    
    # Medications and treatments
    "medication", "medicine", "drug", "prescription", "prescribe", "prescribed",
    "pill", "tablet", "capsule", "dose", "dosage",
    "antibiotic", "painkiller", "pain-killer", "aspirin", "ibuprofen",
    "antidepressant", "antidepressants",
    "side-effect", "side-effects", "reaction", "allergic-reaction",
    "surgery", "operation", "operate", "procedure", "surgical",
    
    # Medical professionals
    "specialist", "surgeon", "cardiologist", "dermatologist",
    "neurologist", "oncologist", "pediatrician",
    "gynecologist", "obstetrician", "urologist", "orthopedist",
    "ophthalmologist", "dentist", "dental",
    "resident", "chief", "chief-resident",
    
    # Exercise and physical activity
    "exercise", "exercising", "workout", "working-out", "gym",
    "run", "running", "jog", "jogging", "walk", "walking",
    "swim", "swimming", "bike", "biking", "cycle", "cycling",
    "yoga", "stretch", "stretching", "cardio", "aerobic",
    
    # Diet and nutrition
    "diet", "dieting", "nutrition", "nutritionist", "dietitian",
    "eat", "eating", "food", "meal",
    "weight", "lose-weight", "gain-weight", "weight-loss", "weight-gain",
    "obesity", "obese", "overweight", "underweight", "bmi",
    "calorie", "calories", "protein", "carbohydrate", "fat", "vitamin", "mineral",
    "vegetable", "fruit", "healthy-eating",
    
    # Harmful behaviors
    "smoke", "smoking", "smoker", "cigarette", "tobacco", "nicotine",
    "alcohol", "alcoholic", "drink", "drinking", "drunk",
    "drug", "drugs", "substance", "addiction", "addicted", "addict",
    
    # Sleep
    "sleep", "sleeping", "insomnia", "sleepless", "rest", "resting",
    "tired", "exhausted", "fatigue", "fatigued",
    
    # Preventive care
    "vaccine", "vaccination", "vaccinate", "vaccinated", "immunization",
    "screening", "mammogram", "colonoscopy",
    "preventive", "prevention", "prevent", "preventing",
    
    # Emergency and urgent care
    "emergency", "urgent", "ambulance", "er", "emergency-room",
    "icu", "intensive-care", "critical",
    
    # Digestive health
    "digestion", "digest", "digestive", "stomach-ache",
    "appetite", "hungry", "hunger", "nausea", "nauseous",
    "bloat", "bloated", "bloating", "gas",
    "acid-reflux", "heartburn", "indigestion",
    "ulcer", "crohn", "ibs", "colitis",
    "celiac", "gluten", "lactose", "intolerance", "intolerant",
    
    # Women's health
    "period", "menstruation", "menstrual", "menstruate",
    "cycle", "pms", "cramp", "cramping",
    "endometriosis", "pcos", "ovarian",
    "fertility", "fertile", "infertility", "infertile",
    "pregnant", "pregnancy", "miscarriage",
    "contraception", "birth-control",
    
    # Aging and elderly health
    "age", "aging", "elderly", "senior",
    "dementia", "alzheimer", "alzheimers",
    "memory", "memory-loss", "cognitive", "cognition",
    "mobility", "balance", "fall", "falling", "fallen",
    
    # Body functions and vitality
    "energy", "energetic", "vitality", "vigor",
    "strength", "strong", "weak", "weakness",
    "breathe", "breathing", "breath",
    
    # Sensory health
    "vision", "sight", "see", "seeing", "blind", "blindness",
    "glasses", "contact", "contact-lens",
    "hearing", "hear", "deaf", "deafness", "hearing-aid",
    "tinnitus", "smell", "taste",
    
    # Skin conditions
    "acne", "pimple", "eczema", "psoriasis", "rosacea",
    "wrinkle", "scar", "scarring", "mole", "melanoma",
    "sunburn", "dermatitis",
    
    # Respiratory
    "respiratory", "pneumonia", "bronchitis", "emphysema", "copd",
    "oxygen", "inhale", "inhaler", "exhale", "wheeze", "wheezing",
    
    # Pain types
    "chronic-pain", "acute-pain", "nerve-pain", "neuropathy",
    "fibromyalgia", "back-pain", "neck-pain", "joint-pain",
    
    # Health monitoring
    "blood-pressure", "pulse", "heart-rate", "temperature",
    "blood-sugar", "glucose", "glucose-level", "a1c",
    "cholesterol-level", "test-result", "lab-result",
    
    # Alternative medicine
    "herbal", "herb", "remedy", "natural", "holistic",
    "acupuncture", "chiropractor", "chiropractic",
    "massage", "physical-therapist",
    
    # Medical procedures
    "x-ray", "scan", "mri", "ct-scan", "ultrasound",
    "biopsy", "blood-test", "blood-work",
    "chemotherapy", "radiation", "radiotherapy",
    
    # Health insurance
    "insurance", "health-insurance", "coverage", "covered",
    "copay", "co-pay", "deductible", "premium", "claim",
    
    # Recovery and wellness
    "convalescence", "recuperate", "recuperating",
    "improve", "improving", "improvement", "better", "worse", "worsen",
    "progress", "regain", "restore", "bounce-back",
    
    # General health concerns
    "concern", "concerned", "worry", "worried", "anxious",
    "scare", "scared", "fear", "afraid",
    "serious", "severe", "critical", "chronic",
    "survive", "survival", "survivor",
    "result", "results", "test-result",
    "protect", "protection", "protective",
    
    # Body image and wellness
    "body-image", "appearance", "self-esteem",
    "weight", "shape", "size"
]

FINANCE = [
    # Money basics
    "money", "finance", "financial", "cash", "currency", "dollar", "cent",
    "wealth", "wealthy", "rich", "poor", "poverty", "broke", "bankrupt", "bankruptcy",
    
    # Income and earnings
    "income", "salary", "wage", "pay", "payment", "paycheck", "earn", "earning",
    "revenue", "profit", "gain", "bonus", "commission", "tip", "overtime",
    "raise", "promotion", "increase", "decrease", "cut", "reduction",
    
    # Employment and job
    "job", "work", "career", "employment", "employ", "employer", "employee",
    "unemployed", "unemployment", "jobless", "laid-off", "layoff",
    "hire", "hired", "fire", "fired", "resign", "quit", "quitting",
    "retire", "retirement", "pension", "401k", "benefits", "compensation",
    "boss", "manager", "supervisor", "colleague", "coworker",
    
    # Expenses and costs
    "expense", "expenses", "cost", "costs", "spend", "spending",
    "buy", "buying", "purchase", "purchasing", "shopping",
    "price", "prices", "expensive", "cheap", "afford", "affordable",
    "budget", "budgeting", "bill", "bills",
    
    # Housing costs
    "rent", "rental", "renting", "landlord", "tenant", "lease", "leasing",
    "mortgage", "mortgages", "down-payment", "closing-cost",
    "property-tax", "hoa", "eviction", "evict", "foreclosure", "foreclose",
    
    # Utilities and subscriptions
    "utility", "utilities", "electricity", "electric-bill",
    "water", "water-bill", "gas", "gas-bill",
    "phone", "phone-bill", "internet", "internet-bill",
    "cable", "subscription", "subscriptions", "membership", "fee", "fees", "charge", "charges",
    
    # Banking
    "bank", "banking", "banker", "account", "checking", "checking-account",
    "saving", "savings", "savings-account",
    "deposit", "depositing", "withdraw", "withdrawal", "withdrawing",
    "balance", "overdraft", "overdrawn", "atm",
    "transaction", "transactions", "transfer", "wire", "wire-transfer",
    
    # Debt and owing
    "debt", "debts", "owe", "owing", "owed", "borrow", "borrowing", "borrowed",
    "loan", "loans", "lend", "lending", "lender", "borrower",
    "creditor", "debtor", "liability", "liabilities",
    "payment-plan", "installment", "installments",
    "default", "defaulted", "delinquent", "delinquency",
    "collection", "collections", "collector", "debt-collector",
    "garnish", "garnishment", "wage-garnishment",
    
    # Credit cards and credit
    "credit", "credit-card", "credit-cards", "card", "cards",
    "visa", "mastercard", "amex", "discover",
    "credit-score", "credit-report", "fico", "score",
    "apr", "interest", "interest-rate", "rate", "rates",
    "balance-transfer", "cash-advance",
    "limit", "credit-limit", "utilization",
    "minimum-payment", "statement", "due-date", "late-fee", "late-payment",
    
    # Specific loan types
    "student-loan", "student-loans", "student-debt",
    "auto-loan", "car-loan", "car-payment",
    "personal-loan", "payday-loan",
    "home-loan", "refinance", "refinancing",
    "consolidate", "consolidation", "debt-consolidation",
    "principal", "term", "fixed-rate", "variable-rate", "adjustable",
    
    # Investing and wealth building
    "invest", "investing", "investment", "investments", "investor",
    "portfolio", "stock", "stocks", "share", "shares", "equity",
    "bond", "bonds", "mutual-fund", "mutual-funds",
    "etf", "index-fund", "dividend", "dividends",
    "yield", "return", "returns", "roi",
    "capital-gain", "capital-gains", "capital-loss",
    "bull-market", "bear-market", "market", "stock-market",
    "volatility", "risk", "risky", "diversify", "diversification",
    "asset", "assets", "allocation",
    
    # Trading
    "trade", "trading", "trader", "broker", "brokerage",
    "buy", "sell", "long", "short",
    "option", "options", "call", "put", "future", "futures",
    "derivative", "derivatives", "commodity", "commodities",
    "forex", "currency", "exchange",
    "cryptocurrency", "crypto", "bitcoin", "blockchain",
    "floor", "trading-floor", "pit", "crash", "market-crash",
    "spike", "surge", "rally", "drop",
    
    # Real estate
    "house", "home", "property", "real-estate",
    "apartment", "condo", "condominium",
    "buy-house", "sell-house", "home-buying", "home-selling",
    "appraisal", "appraised", "inspection",
    "equity", "home-equity", "appreciation", "depreciation",
    "title", "deed", "escrow", "closing",
    
    # Retirement planning
    "retirement", "retire", "retiring", "retired",
    "401k", "ira", "roth", "roth-ira", "traditional-ira",
    "pension", "pensions", "annuity", "annuities",
    "social-security", "medicare",
    "nest-egg", "distribution", "rmd", "required-minimum-distribution",
    
    # Taxes
    "tax", "taxes", "taxable", "taxation",
    "deduction", "deductions", "deductible", "tax-deduction",
    "credit", "tax-credit", "refund", "tax-refund",
    "return", "tax-return", "file", "filing",
    "irs", "federal", "federal-tax", "state", "state-tax",
    "income-tax", "capital-gains-tax", "property-tax", "sales-tax",
    "withholding", "w2", "1099", "schedule",
    "audit", "audited", "accountant", "cpa", "tax-preparer",
    
    # Insurance
    "insurance", "insure", "insured", "policy", "policies",
    "premium", "premiums", "deductible", "coverage", "covered",
    "claim", "claims", "beneficiary",
    "life-insurance", "health-insurance", "dental-insurance",
    "auto-insurance", "car-insurance", "home-insurance", "renters-insurance",
    "disability-insurance", "liability", "liability-insurance",
    
    # Business and entrepreneurship
    "business", "businesses", "company", "companies",
    "corporation", "llc", "partnership", "sole-proprietor",
    "entrepreneur", "entrepreneurship", "startup", "start-up",
    "small-business", "franchise",
    "revenue", "revenues", "profit", "profits", "loss", "losses",
    "margin", "margins", "gross", "net", "overhead",
    "expense", "expenses", "liability", "liabilities",
    "balance-sheet", "income-statement", "cash-flow",
    "quarter", "quarterly", "fiscal-year", "stakeholder", "shareholder",
    "conference", "meeting", "presentation", "pitch",
    
    # Saving and planning
    "save", "saving", "savings", "savings-account",
    "emergency-fund", "rainy-day", "nest-egg",
    "goal", "goals", "target", "plan", "planning", "financial-plan",
    "financial-planner", "advisor", "financial-advisor",
    "wealth-management", "asset-management",
    
    # Economic concepts
    "economy", "economic", "recession", "depression",
    "inflation", "deflation", "deflate", "inflate",
    "interest-rate", "federal-reserve", "fed",
    "monetary-policy", "fiscal-policy",
    "gdp", "unemployment-rate", "consumer-price-index", "cpi",
    "efficiency", "efficient", "innovation", "innovative",
    "compete", "competition", "competitive", "competitor",
    "driven", "drive", "opportunity", "opportunities",
    
    # Financial problems and struggles
    "struggle", "struggling", "hardship", "difficulty", "difficulties",
    "tight", "short", "pinch", "crisis", "financial-crisis",
    "emergency", "unexpected", "surprise", "setback",
    "behind", "late", "overdue", "past-due",
    "cannot-afford", "can't-afford", "unable", "impossible",
    
    # Fraud and security
    "scam", "scams", "scammed", "fraud", "fraudulent",
    "identity-theft", "stolen", "theft",
    "phishing", "hack", "hacked", "breach", "compromised",
    
    # Wealth and poverty
    "millionaire", "billionaire", "fortune",
    "accumulate", "accumulation", "grow", "growth", "build", "building",
    "compound", "compounding", "passive-income", "residual",
    
    # Financial goals and milestones
    "milestone", "achievement", "accomplish", "reach", "attain",
    "save-for", "plan-for", "prepare", "preparation",
    "long-term", "short-term", "medium-term",
    
    # Budgeting
    "budget", "budgeting", "allocate", "allocation",
    "track", "tracking", "monitor", "monitoring",
    "category", "categories", "limit", "cap",
    "overspend", "overspending", "underspend",
    
    # Financial education
    "learn", "learning", "education", "literacy", "financial-literacy",
    "knowledge", "understand", "understanding", "research",
    
    # Financial institutions
    "credit-union", "institution", "fintech",
    "online-bank", "traditional-bank",
    "wall-street", "stock-exchange",
    
    # Investment terms
    "dow", "s&p", "nasdaq", "index", "indices",
    "sector", "sectors", "industry",
    "fund", "funds", "reit", "reits",
    "treasury", "treasuries", "municipal", "corporate", "government",
    
    # Financial ratios and metrics
    "ratio", "ratios", "debt-to-income", "price-to-earnings", "pe-ratio",
    "dividend-yield", "expense-ratio",
    "liquidity", "solvency", "profitability",
    
    # Money management
    "manage", "management", "managing", "control", "controlling",
    "organize", "organizing", "strategy", "strategies",
    
    # Financial advice
    "advice", "advise", "tip", "tips", "recommend", "recommendation",
    "suggestion", "suggestions", "guidance", "consult", "consultation",
    "expert", "professional", "specialist",
    
    # Frugality and savings
    "frugal", "thrifty", "economical", "prudent",
    "save-money", "cut-cost", "reduce-spending",
    "deal", "deals", "discount", "discounts", "sale", "sales",
    "coupon", "coupons", "bargain", "bargains",
    
    # Financial stress
    "stress", "stressed", "stressful", "worry", "worried", "worrying",
    "anxiety", "anxious", "concern", "concerned",
    "overwhelm", "overwhelmed", "overwhelming",
    
    # Financial freedom and security
    "freedom", "financial-freedom", "independence", "financial-independence",
    "security", "financial-security", "stability", "stable",
    "comfortable", "comfort", "cushion", "safety-net",
    
    # Bankruptcy and debt relief
    "bankruptcy", "bankrupt", "chapter-7", "chapter-11", "chapter-13",
    "debt-relief", "debt-settlement", "negotiate", "negotiation",
    
    # Paycheck and compensation
    "paycheck", "paychecks", "payroll", "direct-deposit",
    "gross-pay", "net-pay", "take-home", "take-home-pay",
    
    # Career and income
    "career-change", "job-search", "job-hunting",
    "interview", "offer", "job-offer", "contract", "negotiate-salary",
    "side-hustle", "side-job", "freelance", "freelancing", "gig",
    
    # Major purchases
    "car", "vehicle", "automobile", "purchase",
    "appliance", "furniture", "repair", "repairs",
    
    # Financial independence
    "fire", "financial-independence-retire-early",
    "early-retirement", "passive-income"
]
