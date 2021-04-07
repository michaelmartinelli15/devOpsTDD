from selenium import webdriver
import unittest
browser = webdriver.Firefox()


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Michael was looking for a good way to keep track of school and work responsibilities
        # He found this cool online to-do app

        # After visiting the site, Michael noticed the word "To-Do" in the page titel

        # He is asked to enter a to-do item

        # He types "Finish DevOps Assignment"

        # After hitting enter, the page refreshes and the page now lists "1: Finish DevOps Assignment"

        # There is still a text box to enter another to do item

        # After leaving for a while, Michael revisits the website, hoping his list will still be there
        # It is!

        # Michael is satisfied and stops worrying about it
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
