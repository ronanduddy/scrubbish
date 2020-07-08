from .page import Page


class Properties(Page):
    def __init__(self, area):
        self.current_index = 0
        self.previous_index = 0
        super().__init__(f"/houses-for-sale/{area}")

    def more(self):
        return self.previous_index < self._zeroed_div_count() or self._next_button()

    def next_uri(self):
        if self.previous_index == self._zeroed_div_count():
            self._next_page()
            self._reset_counters()

        self._advance_uri()
        uri = self._previous_div().find_parent().get("href")

        return uri

    def pagination(self):
        return self.content().find_all("span", class_="pgheader-currentpage")[0].text

    def _next_button(self):
        return self.content().find("a", class_="btn paging-next")

    def _advance_uri(self):
        self.previous_index = self.current_index
        self.current_index += 1

    def _reset_counters(self):
        self.previous_index = 0
        self.current_index = 0

    def _zeroed_div_count(self):
        return len(self._divs()) - 1

    def _divs(self):
        return self.content().find_all("div", class_="propbox-details")

    def _previous_div(self):
        return self._divs()[self.previous_index]

    def _next_page(self):
        try:
            uri = self._next_button().get("href")
            self.next(uri)
        except AttributeError:
            print("Next page not found")
