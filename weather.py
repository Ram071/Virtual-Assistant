from requests_html import HTMLSession


def Weather(query="Patna"):
    """
    Get current weather information for a city.

    Example:
        Weather()
        Weather("Chennai")
        Weather("Puducherry")
    """

    session = HTMLSession()

    url = f"https://www.google.com/search?q=weather+{query}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/106.0.0.0 Safari/537.36"
        )
    }

    try:
        response = session.get(
            url,
            headers=headers,
            timeout=10
        )

        temperature = response.html.find(
            "span#wob_tm",
            first=True
        )

        unit = response.html.find(
            "div.vk_bk.wob-unit span.wob_t",
            first=True
        )

        description = response.html.find(
            "span#wob_dc",
            first=True
        )

        if not temperature or not unit or not description:
            return f"Sorry, I couldn't find weather information for {query}."

        return (
            f"The weather in {query} is "
            f"{temperature.text}{unit.text}, "
            f"{description.text}."
        )

    except Exception as error:
        return f"Unable to get weather information: {error}"

    finally:
        session.close()


if __name__ == "__main__":
    print(Weather("Patna"))
