import requests
import time
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
from google.genai import errors as genai_errors

API_KEY = ''
MODEL_ID = "gemini-2.5-flash" 
client = genai.Client(api_key=API_KEY)

# The list of all possible URLs to link to
sitemap_urls = [
"/industry-updates/a-new-look-see-whats-changed-at-reverselogix-com/",
"/industry-updates/basics-on-the-future-of-micro-fulfillment/",
"/industry-updates/churn-and-customer-retention/",
"/industry-updates/common-logistics-issues-to-know/",
"/industry-updates/common-shopify-returns-issues/",
"/industry-updates/costs-of-shopify-returns/",
"/industry-updates/dangers-of-subpar-returns-management/",
"/industry-updates/how-a-liberal-policy-lowers-returns-rates/",
"/industry-updates/how-returns-analytics-benefit-you/",
"/industry-updates/how-reverse-logistics-saves-money/",
"/industry-updates/misconceptions-on-serial-returners/",
"/industry-updates/pitfalls-of-substandard-asset-management/",
"/industry-updates/steps-for-reducing-returns-fraud/",
"/industry-updates/tips-for-keeping-shipping-costs-down/",
"/industry-updates/turning-returns-into-a-positive/",
"/industry-updates/how-to-keep-your-reverse-supply-chain-green/",
"/industry-updates/3-ways-to-improve-your-bottom-line-through-reverse-logistics/",
"/industry-updates/the-importance-of-transparency-in-the-reverse-business-cycle/",
"/industry-updates/reverse-logistics-one-year-later-lessons-learned-from-a-pandemic/",
"/industry-updates/how-to-meet-the-changing-expectations-of-todays-consumers/",
"/industry-updates/using-reverse-logistics-to-control-total-cost-of-ownership/",
"/industry-updates/4-reasons-your-yard-management-team-needs-better-software/",
"/industry-updates/3-signs-you-need-reverse-supply-chain-management-help-now/",
"/industry-updates/now-is-the-time-to-implement-a-reverse-logistics-strategy/",
"/industry-updates/whats-a-return-worth-factoring-economics-and-environment-with-reverse-logistics-software/",
"/industry-updates/what-happens-to-your-returned-items-the-answer-could-give-you-a-competitive-advantage/",
"/industry-updates/proactivity-vs-reactivity-in-the-reverse-supply-chain/",
"/industry-updates/are-you-tracking-the-right-reverse-logistics-metrics/",
"/industry-updates/how-to-choose-a-returns-management-system-5-factors/",
"/industry-updates/using-reverse-logistics-to-improve-asset-management/",
"/industry-updates/why-your-coo-wants-a-reverse-logistics-platform/",
"/industry-updates/reverselogix-rms-case-study-global-retailer/",
"/industry-updates/reverselogix-case-study-genesco/",
"/industry-updates/online-shopping-trends-looking-beyond-2021-to-the-future-of-your-business/",
"/industry-updates/why-kitting-consolidation-services-are-the-future-of-retail/",
"/industry-updates/4-reasons-your-business-should-be-managing-its-reverse-logistics-better/",
"/industry-updates/3-ways-a-returns-portal-for-your-company-can-make-life-easier/",
"/industry-updates/tapping-the-open-box-market-to-improve-revenue-streams/",
"/industry-updates/can-reverse-logistics-help-improve-your-customer-reviews-ratings/",
"/industry-updates/getting-the-perfect-reverse-logistics-platform/",
"/industry-updates/are-you-using-reverse-logistics-to-manage-product-returns/",
"/industry-updates/how-returns-can-kill-your-online-stores-profitability-and-how-to-avoid-it/",
"/industry-updates/are-you-prepared-for-a-surge-in-online-holiday-shopping-and-returns/",
"/industry-updates/is-reverse-logistics-a-core-competency-or-an-afterthought-in-your-business/",
"/industry-updates/how-to-scale-your-returns-and-after-sales-care-management/",
"/industry-updates/3-reasons-to-use-kitting-consolidation-software-at-your-warehouses/",
"/industry-updates/preparing-for-returns-in-a-covid-holiday-shopping-season/",
"/industry-updates/are-reverse-logistics-wasting-your-companys-money/",
"/industry-updates/how-to-make-holiday-shopping-season-more-profitable-for-your-online-retail-shop/",
"/industry-updates/how-your-customers-really-feel-about-returns/",
"/industry-updates/why-your-customer-experience-director-wants-a-reverse-logistics-platform/",
"/industry-updates/business-areas-returns-data-can-impact/",
"/industry-updates/study-reveals-retailers-returns-costs-how-to-minimize/",
"/industry-updates/reverselogix-case-study-samsonite/",
"/industry-updates/warehouse-employees-love-reverselogix-rms/",
"/industry-updates/returnly-sunset-holistic-returns-management-solutions/",
"/industry-updates/b2c-returns-amer-sports/",
"/industry-updates/easing-the-holiday-rush-repairs-management-software/",
"/industry-updates/using-technology-for-customer-facing-reverse-logistics-challenges/",
"/industry-updates/managing-returns-why-most-companies-use-the-wrong-tools/",
"/industry-updates/are-you-tracking-the-right-metrics-for-your-reverse-logistics/",
"/industry-updates/4-keys-to-managing-returns-in-a-manufacturing-facility/",
"/industry-updates/the-importance-of-communications-in-the-returns-management-process/",
"/industry-updates/3-ways-to-make-returns-profitable-for-your-business/",
"/industry-updates/why-returns-management-is-more-important-than-ever-in-2021/",
"/industry-updates/five-ways-to-improve-returns-processes-in-2021/",
"/industry-updates/4-things-your-e-commerce-site-needs-as-online-sales-increase/",
"/industry-updates/3-steps-to-improve-operational-efficiency-in-returns-management/",
"/industry-updates/are-you-winning-the-customer-experience-battle-with-your-competitors/",
"/industry-updates/the-benefits-of-a-comprehensive-reverse-logistics-management-software/",
"/industry-updates/streamlining-rma-initiation-management-and-customization/",
"/industry-updates/what-is-rma/",
"/industry-updates/what-is-warehouse-management/",
"/industry-updates/4-reverse-logistics-reports-that-every-cfo-needs-to-see/",
"/industry-updates/convincing-your-c-suite-that-you-need-reverse-logistics-software/",
"/industry-updates/key-advantages-of-a-completely-customizable-returns-portal/",
"/industry-updates/ship-track-notify-how-returns-forwarding-builds-trust-with-customers/",
"/industry-updates/selling-on-a-marketplace-3-tips-for-managing-returns/",
"/industry-updates/quadrant-solutions-rms-analysis/",
"/industry-updates/reverselogix-rms-case-study-amer-sports/",
"/industry-updates/valiantceo-interview-gaurav-saran/",
"/industry-updates/retailist-ai-retail-gaurav-saran/",
"/industry-updates/revolutionizing-returns-ceo-journey/",
"/industry-updates/gaurav-saran-of-reverselogix-on-how-to-create-a-fantastic-retail-experience-that-keeps-bringing-customers-back-for-more/",
"/industry-updates/industry-updates-revamp-reverse-logistics-for-returns-season/",
"/industry-updates/4-ways-reverse-logistics-can-help-improve-the-supply-chain/",
"/industry-updates/kitting-consolidation-efficient-returns-management/",
"/industry-updates/logistics-vs-supply-chain-management/",
"/industry-updates/retail-bracketing-impacts/",
"/industry-updates/recommerce-program-benefits/",
"/industry-updates/reverselogix-vs-returnlogic/",
"/industry-updates/achieve-your-sustainability-goals-using-reverse-logistics/",
"/industry-updates/auto-route-product-returns/",
"/industry-updates/returns-management-tips/",
"/industry-updates/visibility-gap-maximize-retail-success/",
"/industry-updates/asset-management-challenges-reverse-logistics/",
"/industry-updates/putting-a-cx-focus-into-your-reverse-business/",
"/industry-updates/five-ways-improve-returns-processes/",
"/industry-updates/4-things-you-probably-dont-know-about-reverse-logistics/",
"/industry-updates/the-benefits-of-automation-in-reverse-logistics/",
"/industry-updates/how-are-retailers-adapting-to-consumer-demand-for-preowned-products/",
"/industry-updates/payment-reversals-refund-chargeback-reversal-transaction/",
"/industry-updates/product-returns-hidden-costs/",
"/industry-updates/returns-management-vs-reverse-logistics-understanding-the-difference/",
"/industry-updates/ripple-effect-of-girl-math-analyzing-impact-on-consumer-behavior-retail-returns/",
"/industry-updates/the-role-of-reverse-logistics-in-recommerce/",
"/industry-updates/why-is-return-policy-important-for-e-commerce-business/",
"/industry-updates/4-reasons-every-third-party-logistics-warehouse-needs-a-returns-management-system/",
"/industry-updates/4-steps-to-a-smoother-holiday-shopping-returns-season-for-online-retailers/",
"/industry-updates/how-these-3-factors-will-influence-holiday-shopping-and-returns/",
"/industry-updates/reverselogix-roi-calculator/",
"/industry-updates/the-five-rs-of-returns-management/",
"/industry-updates/using-the-right-stock-rotation-tools-keeps-holiday-inventory-fresh/",
"/industry-updates/improving-the-customer-return-experience-to-build-customer-loyalty/",
"/industry-updates/5-reasons-all-3pl-warehouses-should-provide-returns-management/",
"/industry-updates/online-return-costs/",
"/industry-updates/reverselogix-vs-narvar/",
"/industry-updates/how-preorders-work-in-ecommerce/",
"/industry-updates/reverse-logistics-software-is-critical-for-coordination/",
"/industry-updates/why-do-customers-make-returns/",
"/industry-updates/why-use-returns-technology-microfulfillment-centers/",
"/industry-updates/what-is-last-mile-delivery/",
"/industry-updates/customer-returns-automation-a-guide/",
"/industry-updates/3-things-customers-expect-from-online-retailers/",
"/industry-updates/5-reasons-why-your-returns-management-process-is-failing/",
"/industry-updates/how-to-improve-product-registration-rates/",
"/industry-updates/exploring-reverse-logistics-platforms-a-look-at-reverselogixs-system/",
"/industry-updates/what-is-inventory-shrinkage-causes-prevention/",
"/industry-updates/is-returns-avoidance-truly-a-viable-strategy/",
"/industry-updates/how-to-leverage-data-analytics-for-optimized-reverse-logistics-operations/",
"/industry-updates/inventory-turnover-ratio-defined/",
"/industry-updates/using-reverse-logistics-to-build-customer-loyalty/",
"/industry-updates/solving-the-mounting-e-commerce-returns-problem/",
"/industry-updates/what-is-order-management/",
"/industry-updates/improve-customer-retention-reverse-logistics/",
"/industry-updates/strategies-for-reducing-product-return-rate/",
"/industry-updates/wms-vs-rms/",
"/industry-updates/chat-gpt-returns-management/",
"/industry-updates/b2b-returns-management-software-benefits/",
"/industry-updates/the-case-for-business-intelligence-in-reverse-logistics/",
"/industry-updates/back-to-school-and-holiday-prep-using-business-intelligence-to-minimize-the-returns-hassle/",
"/industry-updates/are-you-leveraging-reverse-logistics-bi/",
"/industry-updates/business-intelligence-reverse-logistics-efficiency/",
"/industry-updates/5-ways-returns-management-improves-profitability-of-the-business/",
"/industry-updates/how-recommerce-is-driving-the-growth-of-circular-economy/",
"/industry-updates/how-reverse-logistics-help-improve-the-customer-experience/",
"/industry-updates/a-complete-guide-to-building-a-successful-product-returns-management-process/",
"/industry-updates/returns-management-can-you-afford-not-to-offer-free-returns/",
"/industry-updates/guide-to-product-returns-data-benefits-and-how-to-acquire-them/",
"/industry-updates/critical-keys-to-succeed-as-a-3pl-provider/",
"/industry-updates/solving-3pl-reverse-logistics-challenges/",
"/industry-updates/the-role-of-data-analytics-in-improving-returns-management/",
"/industry-updates/the-rising-trend-of-online-returns-challenges-and-solutions-for-retailers/",
"/industry-updates/transforming-customer-returns-mastering-reverse-logistics-for-business-success/",
"/industry-updates/beyond-returns-management-unlocking-net-sales-growth-by-addressing-root-causes/",
"/industry-updates/correlation-between-customer-satisfaction-and-return-rates/",
"/industry-updates/overcoming-repair-management-challenges/",
"/industry-updates/the-critical-role-of-analytics-in-your-reverse-logistics/",
"/industry-updates/unraveling-the-complexity-of-b2b-returns-in-a-b2c-world/",
"/industry-updates/redefining-returns-the-new-age-of-reverse-logistics/",
"/industry-updates/reverselogix-vs-loop-returns/",
"/industry-updates/return-policy-best-practices/",
"/industry-updates/flat-rate-shipping-advantages-disadvantages/",
"/industry-updates/return-labels-guide/",
"/industry-updates/5-challenges-all-shippers-using-wms-to-manage-returns-grapple-with/",
"/industry-updates/technology-product-returns/",
"/industry-updates/building-a-customer-centric-returns-experience-key-factors-for-success/",
"/industry-updates/retail-businesses-need-to-think-long-and-hard-on-their-returns-policies-and-reverse-logistics/",
"/industry-updates/addressing-the-challenge-of-increasing-returns-in-a-slow-growth-retail-sector/",
"/industry-updates/enhancing-retail-supply-chains-the-impact-of-leveraging-technology-in-the-reverse-logistics-operation/",
"/industry-updates/mastering-returns-management-key-strategies-for-retailers-in-the-consumer-driven-era/",
"/industry-updates/integrating-reverse-logistics-into-future-retail-business-strategy/",
"/industry-updates/what-to-look-for-when-choosing-a-reverse-logistics-partner/",
"/industry-updates/reverse-logistics-integration-with-forward-fulfillment-a-practical-guide/",
"/industry-updates/product-returns-prevention-avoidance/",
"/industry-updates/5-things-a-reverse-logistics-software-platform-must-have-today/",
"/industry-updates/duty-drawback-guide-recovering-lost-revenue-on-international-returns/",
"/industry-updates/multichannel-returns-reverse-logistics/",
"/industry-updates/returns-drop-off-network-improve-returns-management/",
"/industry-updates/lost-sales-are-eating-your-revenue-heres-what-to-do-about-it/",
"/industry-updates/why-yard-management-team-needs-better-software/",
"/industry-updates/how-tariffs-reshape-reverse-supply-chains/",
"/industry-updates/the-psychology-of-retail-therapy-designing-a-returns-experience-that-heals-not-hurts/",
"/industry-updates/smart-sustainable-packaging-solutions-to-power-circular-returns-and-cut-costs/",
"/industry-updates/the-business-case-for-circular-returns-management/",
"/industry-updates/product-repairs-refurbishments-maximize-processes/",
"/industry-updates/why-reverse-logistics-needs-a-seat-at-the-product-lifecycle-management-plm-table/",
"/industry-updates/product-data-management-for-refurbishment-plms-critical-role/",
"/industry-updates/customer-lifetime-value-define-calculate/",
"/industry-updates/ai-chatbot-simplify-returns/",
"/industry-updates/rethinking-returns-strategy-to-trace-and-tackle-the-why-of-product-returns/",
"/industry-updates/post-purchase-behavior/",
"/industry-updates/fsn-analysis-techniques/",
"/industry-updates/overnight-shipping-options-you-should-know/",
"/industry-updates/7-reasons-why-customers-return-products/",
"/industry-updates/how-to-write-a-retail-return-and-exchange-policy-free-template/",
"/industry-updates/package-damage-who-is-at-fault/",
"/industry-updates/the-role-of-reverse-logistics-in-sustainable-practices/",
"/industry-updates/remanufacturing-and-refurbishment-a-guide-to-the-differences/",
"/industry-updates/navigating-international-returns-best-practices-for-cross-border-e-commerce/",
"/industry-updates/offering-hassle-free-cross-border-returns-to-improve-customer-satisfaction/",
"/industry-updates/the-role-of-regional-warehouses-in-optimizing-cross-border-returns/",
"/industry-updates/the-hidden-cost-of-cross-border-returns-on-e-commerce-profitability/",
"/industry-updates/cross-border-returns-opportunities-challenges-how-to-overcome-it/",
"/industry-updates/how-return-fraud-affects-businesses-and-ways-to-prevent-it/",
"/industry-updates/everything-you-need-to-know-about-a-returns-management-system/",
"/industry-updates/why-reverse-logistics-must-be-reinvented-to-reduce-waste/",
"/industry-updates/warranties-repairs-best-practices/",
"/industry-updates/returns-vs-replacement-how-reverse-logistics-affect-processes/",
"/industry-updates/why-you-need-to-automate-your-reverse-logistics-process/",
"/industry-updates/how-reverse-logistics-builds-customer-loyalty/",
"/industry-updates/what-is-return-fraud/",
"/industry-updates/reverse-logistics-and-boris/",
"/industry-updates/reverse-logistics-automation-partner/",
"/industry-updates/counterfeit-returns-are-a-silent-crisis-for-retailers-this-holiday-peak-season/",
"/industry-updates/mitigating-returns-fraud-to-protect-retail-margins-in-fast-fashion/",
"/industry-updates/reverse-logistics-process-issues-finding-fixing/",
"/industry-updates/pros-and-cons-of-a-free-return-policy/",
"/industry-updates/15-ways-an-rms-catches-returns-fraud/",
"/industry-updates/returns-management-for-e-commerce-companies/",
"/industry-updates/how-to-reduce-ecommerce-returns/",
"/industry-updates/revolutionizing-retail-turning-e-commerce-returns-into-revenue/",
"/industry-updates/how-efficient-returns-management-reduces-e-commerce-costs/",
"/industry-updates/best-returns-management-software-ecommerce-brands/",
"/industry-updates/4-ways-rms-creates-an-exceptional-e-commerce-returns/",
"/industry-updates/intelligent-routing-and-automation-the-future-of-e-commerce-returns/",
"/industry-updates/4-ecommerce-trends-impacting-returns-management/",
"/industry-updates/best-practices-for-managing-cross-border-returns/",
"/industry-updates/returns-data-analysis-turning-return-insights-into-profit/",
"/industry-updates/how-to-choose-the-best-reverse-logistics-solution/",
"/industry-updates/the-business-case-for-asset-recovery-in-reverse-logistics/",
"/industry-updates/from-returns-to-revenue-building-an-asset-recovery-strategy/",
"/industry-updates/the-customer-experience-advantage-in-reverse-logistics/",
"/industry-updates/return-types-credits-take-backs-refunds/",
"/industry-updates/returns-management-system-supports-sustainable-returns/",
"/industry-updates/how-returns-shape-customer-loyalty-a-customer-experience-deep-dive/",
"/industry-updates/what-frustrates-customers-most-about-their-returns-experience-and-how-to-fix-it/",
"/industry-updates/how-you-handle-returns-matters-more-than-collecting-them-for-retail-success/",
"/industry-updates/is-free-return-shipping-fueling-the-retail-therapy-boom/",
"/industry-updates/why-returns-forecasting-is-the-missing-link-in-demand-planning/",
"/industry-updates/closing-the-loop-between-sales-forecasting-and-returns-forecasting/",
"/industry-updates/rms-buyers-guide/",
"/industry-updates/how-a-robust-return-to-vendor-rtv-strategy-saves-money/",
"/industry-updates/reducing-the-impact-of-returns-on-your-bottom-line/",
"/industry-updates/the-reverse-logistics-economics-cost-benefit-analysis-for-businesses/",
"/industry-updates/can-e-commerce-supply-chains-benefit-from-automating-customer-returns/",
"/industry-updates/check-your-online-returns-policy-for-these-things-as-holiday-shopping-seasons-starts/",
"/industry-updates/still-recovering-from-the-holiday-returns-crush/",
"/industry-updates/inventory-recovery-steps/",
"/industry-updates/how-to-choose-third-party-logistics-provider/",
"/industry-updates/how-can-ai-driven-reverse-logistics-minimize-fraud-and-personalize-returns-management/",
"/industry-updates/q-commerce-returns-managing-returns-in-the-age-of-quick-commerce/",
"/industry-updates/reverse-logistics-in-the-luxury-industry-managing-luxury-returns/",
"/industry-updates/how-bnpl-returns-shape-returns-management-systems/",
"/industry-updates/how-smart-reverse-logistics-can-save-the-planet-and-your-bottom-line/",
"/industry-updates/how-to-incentivize-exchanges-over-returns/",
"/industry-updates/how-ai-chatbots-for-returns-can-improve-customer-experience/",
"/industry-updates/how-to-streamline-subscription-returns-for-membership-based-businesses/",
"/industry-updates/the-impact-of-fashion-returns-on-reverse-logistics-and-returns-management/",
"/industry-updates/returns-management-impact-customer-retention-churn/",
"/industry-updates/key-returns-metrics-for-successful-returns-management-in-e-commerce/",
"/industry-updates/how-to-calculate-understand-cost-of-goods-sold/",
"/industry-updates/advanced-exchange-service/",
"/industry-updates/designing-a-retail-marketplace-for-easier-returns-and-refurbishment/",
"/industry-updates/the-evolution-of-returns-management-trends-in-2025-and-beyond/",
"/industry-updates/how-returns-processing-management-improves-business-profitability/",
"/industry-updates/reverse-logistics-challenges-in-the-b2b-space/",
"/industry-updates/strategies-for-handling-post-holiday-returns-rush/",
"/industry-updates/return-data-the-three-categories-and-how-to-leverage-it/",
"/industry-updates/11-reasons-to-leverage-technology-solutions-in-your-returns-management/",
"/industry-updates/why-third-party-logistics-warehouses-need-returns-management-system/",
"/industry-updates/7-strategies-for-improving-the-reverse-logistics-process/",
"/industry-updates/impact-of-e-commerce-on-retail-returns-and-reverse-logistics-processes/",
"/industry-updates/analyzing-the-cost-benefit-of-outsourcing-reverse-logistics-operations/",
"/industry-updates/reverse-logistics/",
"/industry-updates/how-does-3pl-work/",
"/industry-updates/what-is-a-3pl-provider/",
"/industry-updates/3pls-and-e-commerce-a-match-made-in-returns-heaven/",
"/industry-updates/why-every-3pl-needs-a-returns-management-system-rms/",
"/industry-updates/why-are-3pls-adding-reverse-logistics-services/",
"/industry-updates/reverselogix-vs-optoro/",
"/industry-updates/cross-border-returns-tariffs-manage-costs/",
"/industry-updates/the-role-of-digital-twins-in-reverse-logistics-optimization/",
"/solutions/better-returns-experience/",
"/solutions/returns-tracking-analytics/",
"/solutions/recommerce/",
"/solutions/improve-margin/",
"/solutions/return-merchandise-authorization-process/",
"/solutions/prevent-returns/",
"/solutions/automate-returns/",
"/solutions/achieve-sustainability-goals/",
"/solutions/return-fraud-prevention/",
"/solutions/reverselogix-partners/",
"/industries/ecommerce/salesforce/",
"/industries/pulse-order-tracking-module/",
"/industries/ecommerce/shopify/",
"/industries/ecommerce/sap/",
"/industries/ecommerce/magento/",
"/industries/ecommerce/netsuite/",
"/industries/ecommerce/woocommerce/",
"/industries/manufacturer-returns-management/",
"/industries/ecommerce/oracle/",
"/industries/ecommerce/fedex/",
"/industries/",
"/industries/retailer-returns-management/",
"/industries/3rd-party-logistics-solutions/",
"/industries/fashion-apparel-returns-management/",
"/industries/car-parts-returns-warranty-management/",
"/industries/electronics-technology-repairs-returns/",
"/industries/ecommerce/",
"/returns-management/smarter-business/automation-standardization/",
"/returns-management/smarter-returns/manage-returns/",
"/returns-management/smarter-business/",
"/returns-management/smarter-business/platform-integrations/",
"/returns-management/smarter-returns/returns-experience/",
"/returns-management/roi-calculator/",
"/returns-management/pricing-plans/",
"/returns-management/smarter-returns/returns-management/",
"/returns-management/smarter-business/business-intelligence-analytics/",
"/returns-management/how-it-works/",
"/returns-management-resources/",
"/warranty-return-software-b2b-b2c/",
"/returns-management/",
"/returns-management/smarter-returns/",
]

# The FULL URL of the page you want to analyze
target_page_url = "https://www.reverselogix.com/industry-updates/customer-returns-automation-a-guide/"

# --- Fetch Live HTML ---
print(f"📡 Fetching HTML from: {target_page_url}")

# This tells the website we are a standard browser, preventing the 403 error.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', # Updated User-Agent
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1', # Do Not Track header
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

try:
    response = requests.get(target_page_url, headers=headers)
    response.raise_for_status() # Raise an error for bad responses (4xx or 5xx)

    page_html = response.text
    print("✅ HTML content fetched successfully!")

except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching URL: {e}")
    exit() # Exit the script if the URL can't be fetched

# --- Build the Prompt for Gemini ---
sitemap_string = "\n".join(sitemap_urls)
source_url = "/" + target_page_url.split(".com/")[-1]

prompt = f"""
You are an SEO expert specializing in internal linking strategy.

I will provide you with three pieces of data:
1. The [SOURCE_URL], which is the page I am analyzing.
2. A [SITEMAP_URLS] list, which contains all the valid pages on my website that you can link to.
3. The [PAGE_HTML] for the specific page I am analyzing.

Your task is to analyze the [PAGE_HTML] and identify phrases that are strong candidates for new internal links. For each candidate you identify, you must find the single most relevant URL from the [SITEMAP_URLS] list to be the link's destination. Use the URL slug and page context to determine relevance.

Do not suggest links that already exist in the HTML.

Present your findings as a Markdown table with three columns: "Source URL", "Suggested Anchor Text", and "Suggested Destination URL".

If you find no opportunities, return the single word "None".

---

**[SOURCE_URL]:**
{source_url}

**[SITEMAP_URLS]:**
{sitemap_string}

**[PAGE_HTML]:**
{page_html}
"""

# --- Call the API and Get the Result ---
print("\n🤖 Contacting Gemini for suggestions...")

try:
    # Use the client.models.generate_content method for the new SDK
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )

    print("\n✨ Internal Linking Suggestions:")
    print(response.text)

except Exception as e:
    print(f"❌ An error occurred: {e}")