import spacy
from spacy.matcher import Matcher
#model loading
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)


#training tokens
pattern_categories = ["trends", "trend", "pattern", "patterns", "categories", "category", "categorize"]
pattern_all = ["summary", "summarize", "correlation", "correlations", "each", "other", "overall"]
pattern_anomalies = ["outlier", "outliers"]
pattern_months = ["seasonality", "seasonalities", "growth", "decline", "declines", "cluster", "group", "clusters", "groups", "interval", "intervals", "season", "seasons", "weather"]
pattern_country = ["geographical", "regions", "region"]
pattern_churn = ["customer", "customers", "churn", "churning", "churns"]
pattern_salesamount = ["event", "events", "order", "orders", "transaction", "transactions", "pricing", "pricings", "price", "prices", "discount", "discounts"]
pattern_conversion = ["conversion", "conversions"]
pattern_rating = ["rating", "ratings"]
pattern_price = ["stock", "stocks"]
pattern_campaignname = ["advertising", "advertize", "advertise", "campaign", "campaigns"]
pattern_status = ["subscription", "subscriptions", "subscription", "subscriptions"]
pattern_socialmedia = ["social", "media"]
pattern_marks = ["educational", "education"]
pattern_shipping = ["shipping", "shippings"]
pattern_customerid = ["repeat", "repeats"]
pattern_paymentmethods = ["payment method","payment", "payments", "method", "methods", ]

# Create patterns for each category
patterns_categories = [{"LOWER": {"in": pattern_categories}}]
patterns_all = [{"LOWER": {"in": pattern_all}}]
patterns_anomalies = [{"LOWER": {"in": pattern_anomalies}}]
patterns_months = [{"LOWER": {"in": pattern_months}}]
patterns_country = [{"LOWER": {"in": pattern_country}}]
patterns_churn = [{"LOWER": {"in": pattern_churn}}]
patterns_salesamount = [{"LOWER": {"in": pattern_salesamount}}]
patterns_conversion = [{"LOWER": {"in": pattern_conversion}}]
patterns_rating = [{"LOWER": {"in": pattern_rating}}]
patterns_price = [{"LOWER": {"in": pattern_price}}]
patterns_campaignname = [{"LOWER": {"in": pattern_campaignname}}]
patterns_status = [{"LOWER": {"in": pattern_status}}]
patterns_socialmedia = [{"LOWER": {"in": pattern_socialmedia}}]
patterns_marks = [{"LOWER": {"in": pattern_marks}}]
patterns_shipping = [{"LOWER": {"in": pattern_shipping}}]
patterns_customerid = [{"LOWER": {"in": pattern_customerid}}]
patterns_paymentmethods = [{"LOWER": {"in": pattern_paymentmethods}}]


#model training and adding to pipeline
matcher.add("category", [patterns_categories])
matcher.add("all", [patterns_all])
matcher.add("anomalies", [patterns_anomalies])
matcher.add("months", [patterns_months])
matcher.add("country", [patterns_country])
matcher.add("churn", [patterns_churn])
matcher.add("sales amount", [patterns_salesamount])
matcher.add("conversion", [patterns_conversion])
matcher.add("rating", [patterns_rating])
matcher.add("price", [patterns_price])
matcher.add("campaign name", [patterns_campaignname])
matcher.add("status", [patterns_status])
matcher.add("social media", [patterns_socialmedia])
matcher.add("marks", [patterns_marks])
matcher.add("shipping", [patterns_shipping])
matcher.add("customer ID", [patterns_customerid])
matcher.add("payment methods", [patterns_paymentmethods])



#prompt parsing
doc = nlp("How do different payment methods impact online transaction completion rates")
matches = matcher(doc)

for match_id, start, end in matches:
    span = doc[start:end]
    label = doc.vocab.strings[match_id]
    print({span.text}, label)
    
