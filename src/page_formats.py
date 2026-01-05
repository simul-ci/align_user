"""
Page/state format templates for different domains.

- Recommendation Domains (MovieLens, Steam, AmazonBook)
- OPeRA / Web-Shopping Domains
"""

from __future__ import annotations


# ---------------------------------------------------------------------
# Page Format: Recommendation Domains (MovieLens, Steam, AmazonBook)
# ---------------------------------------------------------------------

PAGE_FORMAT_RECOMMENDATION = """PAGE {page_number}
{items_block}
"""

PAGE_ITEM_FORMAT_RECOMMENDATION = """<- {item_title} -> <- History ratings: {item_rating} -> <- Summary: {item_description} -> <- Similar items: {similar_items} ->"""


def build_page_recommendation(page_number: int, items: list) -> str:
    """
    Build a recommendation-domain page state from a list of item dicts.

    Each item dict should have keys: item_title, item_rating, item_description, similar_items.
    similar_items should be a string like "**Title1 (4/5)**, **Title2 (3/5)**" or empty.
    """
    items_block = "\n".join(
        PAGE_ITEM_FORMAT_RECOMMENDATION.format(
            item_title=item.get("item_title", "Unknown"),
            item_rating=item.get("item_rating", "N/A"),
            item_description=item.get("item_description", ""),
            similar_items=item.get("similar_items", ""),
        )
        for item in items
    )
    return PAGE_FORMAT_RECOMMENDATION.format(page_number=page_number, items_block=items_block)


# ---------------------------------------------------------------------
# Page Format: OPeRA / Web-Shopping Domains
# ---------------------------------------------------------------------

PAGE_FORMAT_OPERA = """PAGE {page_number}
CONTEXT: {page_context}
PRODUCTS:
{products_block}
INTERACTIVE ELEMENTS (semantic IDs):
{semantic_ids}
"""

PAGE_PRODUCT_FORMAT_OPERA = """<- {product_title} -> <- Price: {price} -> <- Availability: {availability} -> <- Details: {short_description} ->"""


def build_page_opera(page_number: int, page_context: str, products: list, semantic_ids: list) -> str:
    """
    Build an OPeRA/web-shopping page state from product list and interactive elements.

    Each product dict should have keys: product_title, price, availability, short_description.
    semantic_ids is a list of strings representing interactive element IDs.
    """
    products_block = "\n".join(
        PAGE_PRODUCT_FORMAT_OPERA.format(
            product_title=prod.get("product_title", "Unknown"),
            price=prod.get("price", "N/A"),
            availability=prod.get("availability", "N/A"),
            short_description=prod.get("short_description", ""),
        )
        for prod in products
    )
    return PAGE_FORMAT_OPERA.format(
        page_number=page_number,
        page_context=page_context,
        products_block=products_block,
        semantic_ids=", ".join(semantic_ids),
    )
