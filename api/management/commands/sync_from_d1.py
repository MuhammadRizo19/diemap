import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import DieMap


class Command(BaseCommand):
    help = 'Sync die map data from Cloudflare D1 into PostgreSQL'

    def handle(self, *args, **options):
        url = (
            f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ACCOUNT_ID}"
            f"/d1/database/{settings.CF_D1_DATABASE_ID}/query"
        )
        headers = {
            "Authorization": f"Bearer {settings.CF_API_TOKEN}",
            "Content-Type": "application/json",
        }

        self.stdout.write("Fetching data from Cloudflare D1...")
        resp = requests.post(
            url,
            json={"sql": "SELECT sapcode, benkam FROM die_map ORDER BY sapcode"},
            headers=headers,
            timeout=30,
        )
        resp.raise_for_status()

        rows = resp.json()["result"][0]["results"]
        self.stdout.write(f"Received {len(rows)} rows from D1.")

        DieMap.objects.all().delete()
        DieMap.objects.bulk_create([
            DieMap(sapcode=r["sapcode"], benkam=r["benkam"])
            for r in rows
        ])

        self.stdout.write(self.style.SUCCESS(f"Done. {len(rows)} rows saved to PostgreSQL."))
